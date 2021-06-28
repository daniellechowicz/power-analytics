import numpy as np
from analysis import features
from nptdms import TdmsFile


class Measurement(features.Features):
    def __init__(
        self,
        path,
        group_name,
        channel_name,
        sampling_rate,
    ):
        self.path = path
        self.group_name = group_name
        self.channel_name = channel_name
        self.sampling_rate = sampling_rate
        self.x_vector, self.data = self.raw()

    def raw(self):
        with TdmsFile.open(self.path) as tdms_file:
            group = tdms_file[self.group_name]
            channel = group[self.channel_name]
            y_vector = channel[:]
            x_vector = np.linspace(0, len(y_vector) / self.sampling_rate, len(y_vector))
            return x_vector, abs(y_vector)
