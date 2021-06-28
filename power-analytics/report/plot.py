from settings import *
import matplotlib.pyplot as plt


class Plot:
    def __init__(self, idle, cutting, x_vector, y_vector, figsize):
        self.idle = idle
        self.cutting = cutting
        self.x_vector = x_vector
        self.y_vector = y_vector
        self.figsize = figsize

        self.sampling_rate = SAMPLING_RATE

    def plot_raw(self, save, path):
        plt.figure(figsize=self.figsize)
        plt.plot(self.x_vector, self.y_vector, linewidth=0.5, color="black")
        plt.axvspan(
            self.cutting["start"], self.cutting["stop"], alpha=0.5, color="#3DFF33"
        )
        plt.axvspan(self.idle["start"], self.idle["stop"], alpha=0.5, color="red")
        plt.xlabel("Zeit [s]", fontsize=FONTSIZE_REPORT)
        plt.ylabel("Leistungsaufnahme [kW]", fontsize=FONTSIZE_REPORT)

        if save == True:
            plt.savefig(path[:-4] + "_full.png", dpi=RESOLUTION)

    def plot_cutting(self, save, path):
        plt.figure(figsize=self.figsize)
        plt.plot(
            self.x_vector,
            self.y_vector,
            linewidth=0.5,
            color="black",
        )
        plt.xlim([self.cutting["start"], self.cutting["stop"]])
        plt.xlabel("Zeit [s]", fontsize=FONTSIZE_REPORT)
        plt.ylabel("Leistungsaufnahme [kW]", fontsize=FONTSIZE_REPORT)

        if save == True:
            plt.savefig(path[:-4] + "_cutting.png", dpi=RESOLUTION)
