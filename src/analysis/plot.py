import matplotlib.pyplot as plt
import os


class Plot:
    def __init__(self, figsize, fontsize, save_dir):
        self.figsize = figsize
        self.fontsize = fontsize
        self.save_path = os.path.join(save_dir, self._filename[:-5])

    def plot_raw(self, save=False):
        plt.figure(figsize=self.figsize)
        plt.plot(self.x_vector, self.data, linewidth=0.5, linestyle="--", color="blue")
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_RAW.png".format(self.save_path), dpi=plt.dpi)

    def plot_butterworth_lowpass_filter(self, cutoff, order, save=False):
        # Get corresponding data
        _, data_processed = self.butterworth_lowpass_filter(cutoff, order)

        plt.figure(figsize=self.figsize)
        plt.plot(
            self.x_vector,
            self.data,
            linewidth=0.5,
            linestyle="--",
            color="blue",
            alpha=0.5,
            label="Raw",
        )
        plt.plot(
            self.x_vector,
            data_processed,
            linewidth=1,
            linestyle="-",
            color="red",
            label="LPF (CF: {} | Order: {})".format(cutoff, order),
        )
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.legend(loc="upper right", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig(
                "{}_LP_{}_{}.png".format(self.save_path, cutoff, order), dpi=plt.dpi
            )

    def plot_fast_fourier_transform(self, save=False):
        # Get corresponding data
        x_vector, data_processed = self.fast_fourier_transform()

        plt.figure(figsize=self.figsize)
        plt.plot(x_vector, data_processed, linewidth=0.5, linestyle="--", color="black")
        plt.xlabel("Frequency [Hz]", fontsize=self.fontsize)
        plt.ylabel("Amplitude [-]", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_FFT.png".format(self.save_path), dpi=plt.dpi)

    def plot_power_spectral_density(self, save=False):
        # Get corresponding data
        x_vector, data_processed = self.power_spectral_density()

        plt.figure(figsize=self.figsize)
        plt.plot(x_vector, data_processed, linewidth=0.5, linestyle="--", color="black")
        plt.xlabel("Frequency [Hz]", fontsize=self.fontsize)
        plt.ylabel("Amplitude [-]", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_PSD.png".format(self.save_path), dpi=plt.dpi)

    def plot_autocorrelation(self, save=False):
        # Get corresponding data
        x_vector, data_processed = self.autocorrelation()

        plt.figure(figsize=self.figsize)
        plt.plot(x_vector, data_processed, linewidth=0.5, linestyle="--", color="black")
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Amplitude [-]", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_AC.png".format(self.save_path), dpi=plt.dpi)

    def plot_moving_average(self, window_size, save=False):
        # Get corresponding data
        x_vector, data_processed = self.moving_average(window_size)

        plt.figure(figsize=self.figsize)
        plt.plot(
            self.x_vector,
            self.data[: len(self.x_vector)],
            linewidth=0.5,
            linestyle="--",
            color="blue",
            alpha=0.5,
            label="Raw",
        )
        plt.plot(
            x_vector,
            data_processed,
            linewidth=1,
            linestyle="-",
            color="red",
            label="MA (WS: {})".format(window_size),
        )
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.legend(loc="upper right", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_MA_{}.png".format(self.save_path, window_size), dpi=plt.dpi)

    def plot_moving_median(self, window_size, save=False):
        # Get corresponding data
        x_vector, data_processed = self.moving_median(window_size)

        plt.figure(figsize=self.figsize)
        plt.plot(
            self.x_vector,
            self.data[: len(self.x_vector)],
            linewidth=0.5,
            linestyle="--",
            color="blue",
            alpha=0.5,
            label="Raw",
        )
        plt.plot(
            x_vector,
            data_processed,
            linewidth=1,
            linestyle="-",
            color="red",
            label="MM (WS: {})".format(window_size),
        )
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.legend(loc="upper right", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_MM_{}.png".format(self.save_path, window_size), dpi=plt.dpi)

    def plot_moving_rms(self, window_size, save=False):
        # Get corresponding data
        x_vector, data_processed = self.moving_rms(window_size)

        plt.figure(figsize=self.figsize)
        plt.plot(
            self.x_vector,
            self.data[: len(self.x_vector)],
            linewidth=0.5,
            linestyle="--",
            color="blue",
            alpha=0.5,
            label="Raw",
        )
        plt.plot(
            x_vector,
            data_processed,
            linewidth=1,
            linestyle="-",
            color="red",
            label="MRMS (WS: {})".format(window_size),
        )
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.legend(loc="upper right", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig(
                "{}_MRMS_{}.png".format(self.save_path, window_size), dpi=plt.dpi
            )

    def plot_peaks(self, period, save=False):
        # Get corresponding data
        x_vector, data_processed = self.peaks(period)

        plt.figure(figsize=self.figsize)
        plt.plot(
            np.linspace(0, len(self.data), len(self.data)),
            self.data,
            linewidth=0.5,
            linestyle="--",
            color="blue",
            label="Raw",
        )
        plt.scatter(
            x_vector, data_processed, s=10, color="orange", marker="*", label="Peaks"
        )
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_PEAKS.png".format(self.save_path), dpi=plt.dpi)

    def plot_hilbert_transform(self, save=False):
        # Get corresponding data
        x_vector, data_processed = self.hilbert_transform()

        plt.figure(figsize=self.figsize)
        plt.plot(
            self.x_vector,
            self.data,
            linewidth=0.5,
            linestyle="--",
            color="blue",
            alpha=0.5,
            label="Raw",
        )
        plt.plot(
            x_vector,
            data_processed,
            linewidth=1,
            linestyle="-",
            color="red",
            label="HT",
        )
        plt.xlabel("Time [s]", fontsize=self.fontsize)
        plt.ylabel("Power consumption [kW]", fontsize=self.fontsize)
        plt.legend(loc="upper right", fontsize=self.fontsize)
        plt.show()

        if save == True:
            plt.savefig("{}_HT.png".format(self.save_path), dpi=plt.dpi)
