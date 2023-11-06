import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, rfft, rfftfreq, fftshift
from scipy.signal import spectrogram
from scipy.signal.windows import hamming
from Source.Common import common_params
import math
    
class System_Core():
    defaults = common_params()
    
    def __init__(self, location, sampling_rate, num_channels, system_name) -> None:
        self.location = location
        self.sampling_rate = sampling_rate
        self.num_channels = num_channels
        self.sys_name = system_name
        
    def create_channel_headings(self, channels):
        headings = []
        for i in range(1, channels + 1):
            headings.append("channel_" + str(i))
        return headings        
        
    def export_df(self):
        heading_names = self.create_channel_headings(channels = self.num_channels)
        raw_data = pd.read_csv(self.location, header = None, names = heading_names)
        # print(raw_data.index)
        time = pd.Series(data = (raw_data.index + 1)/self.sampling_rate , index=raw_data.index)
        time.name = "time"
        data_series = pd.concat([time, raw_data], axis = 1)
        return data_series
        
    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        # data_series.iloc[0:limit, :].plot(x = "time", y = "channel_" + str(channel), figsize=(48, 4))
        data_series.plot(x = "time", y = "channel_" + str(channel))
        plt.ylabel('Magnitude [dB]')
        plt.xlabel('Time [sec]')
        plt.title(f"Time Series for {self.sys_name}, Channel {channel}")
        plt.show()
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        selected_data = data_series[ds_key].to_numpy()
        selected_data = selected_data - np.mean(selected_data)
        yf = fft(selected_data)
        xf = fftfreq(N, 1/self.sampling_rate)
        return (xf, yf)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        selected_data = data_series[ds_key].to_numpy()
        selected_data = selected_data - np.mean(selected_data)
        yf = rfft(selected_data)
        xf = rfftfreq(N, 1/self.sampling_rate)
        return (xf, yf)

    def plot_fft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_fft(channel = channel)
        yf_mag = np.abs(yf)
        # yf_shifted = fftshift(yf_mag)
        plt.plot(xf, yf_mag)
        plt.ylabel('Magnitude')
        plt.xlabel('Frequency [Hz]')
        plt.title(f"FFT for {self.sys_name}, Channel {channel}")
        plt.show()
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_rfft(channel = channel)
        plt.plot(xf, np.abs(yf))
        plt.ylabel('Magnitude')
        plt.xlabel('Frequency [Hz]')
        plt.title(f"RFFT for {self.sys_name}, Channel {channel}")
        plt.show()
        
    def generate_spectrogram(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        num_points = N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        selected_data = data_series[ds_key].to_numpy()
        selected_data = selected_data - np.mean(selected_data)

        nsc = math.floor(num_points/(1500))
        nov = math.floor(nsc/2)
        nff = max(256, pow(2, np.ceil(np.log(nsc)/np.log(2)))) # Round to next highest power of 2.
        
        fig1 = plt.figure()
        f, t, Sxx = spectrogram(
            x = selected_data, 
            fs = self.sampling_rate, 
            window = hamming(nsc), 
            noverlap = nov, 
            nperseg = nsc, nfft = nff, 
            mode = "complex"
        )
        # print("f: ", f.shape)
        # print("t: ", t.shape)
        # print("Sxx: ", Sxx.shape)
        # quit()
        spec = plt.pcolormesh(f, t, 10*np.log10(np.abs(Sxx.T)), cmap = "viridis")
        fig1.colorbar(spec).set_label('Intensity (dB)')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Time [sec]')
        plt.title(f"Spectrogram for {self.sys_name}, Channel {channel}")
        plt.show()
        
        