import matplotlib.pyplot as plt
import numpy as np
import os
from bisect import bisect_left
from bisect import insort
from collections import deque
from itertools import islice
from scipy.fftpack import fft
from scipy.signal import butter
from scipy.signal import find_peaks
from scipy.signal import hilbert
from scipy.signal import lfilter
from scipy.signal import welch


class Features:
    def butterworth_lowpass_filter(self, cut_off=10000, order=5):
        nyq = 0.5 * self.sampling_rate
        normal_cutoff = cut_off / nyq
        b, a = butter(order, normal_cutoff, btype="low", analog=False)

        y_vector = lfilter(b, a, self.data)
        x_vector = np.linspace(0, len(y_vector) / self.sampling_rate, len(y_vector))

        return x_vector, y_vector

    def fast_fourier_transform(self):
        # FFT-related variables
        N = len(self.data)
        t_n = N / self.sampling_rate
        T = t_n / N

        f_values = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
        fft_values = fft(self.data)
        fft_values = 2.0 / N * np.abs(fft_values[0 : N // 2])

        return f_values, fft_values

    def power_spectral_density(self):
        # Calculate Power Spectral Density
        f_values, psd_values = welch(self.data, self.sampling_rate)

        return f_values, psd_values

    def autocorrelation(self):
        # Autocorrelation-related variables
        N = len(self.data)
        t_n = N / self.sampling_rate
        T = t_n / N

        # Get autocorrelation values
        result = np.correlate(self.data, self.data, mode="full")
        y_vector = result[len(result) // 2 :]
        x_vector = np.array([T * jj for jj in range(0, N)])

        return x_vector, y_vector

    def moving_average(self, window_size):
        cumsum = np.cumsum(np.insert(self.data, 0, 0))
        y_vector = (cumsum[window_size:] - cumsum[:-window_size]) / float(window_size)
        x_vector = np.linspace(0, len(y_vector) / self.sampling_rate, len(y_vector))

        return x_vector, y_vector

    def moving_median(self, window_size):
        seq = iter(self.data)
        d = deque()
        s = []
        y_vector = []
        for item in islice(seq, window_size):
            d.append(item)
            insort(s, item)
            y_vector.append(s[len(d) // 2])

        m = window_size // 2

        for item in seq:
            old = d.popleft()
            d.append(item)
            del s[bisect_left(s, old)]
            insort(s, item)
            y_vector.append(s[m])

        x_vector = np.linspace(0, len(y_vector) / self.sampling_rate, len(y_vector))

        return x_vector, y_vector

    def moving_rms(self, window_size):
        data = np.sqrt(np.power(self.data, 2))
        window = np.ones(window_size) / float(window_size)
        y_vector = np.concatenate(
            [
                np.linspace(0, window_size, window_size),
                np.sqrt(np.convolve(data, window, "valid")),
            ]
        )
        x_vector = np.linspace(0, len(y_vector) / self.sampling_rate, len(y_vector))

        return x_vector, y_vector

    def peaks(self, period):
        threshold = 0.25 * np.sqrt(np.mean(np.power(self.data, 2)))
        x_vector, y_vector = find_peaks(
            self.data, height=1.5 * threshold, distance=0.9 * period
        )
        y_vector = y_vector["peak_heights"]

        return x_vector, y_vector

    def hilbert_transform(self):
        analytic_signal = hilbert(self.data)
        amplitude_envelope = np.abs(analytic_signal)
        x_vector = np.linspace(
            0, len(amplitude_envelope) / self.sampling_rate, len(amplitude_envelope)
        )

        return x_vector, amplitude_envelope

    def cutting(self, window_size, period=2400, duration=590, threshold=0.95):
        # Data filtering
        _, y_vector = self.moving_median(window_size)
        x_vector, y_vector = self.peaks(period)

        full_x = []
        full_y = []

        for i, x_vector_i in enumerate(x_vector):
            for j in range(x_vector_i - duration, x_vector_i + duration):
                try:
                    if self.data[j] < threshold * y_vector[i]:
                        continue
                    else:
                        full_x.append(j / self.sampling_rate)
                        full_y.append(self.data[j])
                except:
                    pass

        return full_x, full_y
