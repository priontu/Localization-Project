import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, rfft, rfftfreq, fftshift
# class Store:
#     def __init__(self) -> None:
#         vla_location = "excel_export/raw_data.csv"
#         tla_location = "excel_export/tla_raw.csv"
#         hla_n_location = "excel_export/hla_n_raw.csv"
#         hla_s_location = "excel_export/hla_s_raw.csv"

class common_params:
    def __init__(self) -> None:
        self.default_point_limit = 6000000
        self.default_plot_channel = 1
    
        
class VLA:
    defaults = common_params()
    
    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/vla_raw.csv"
        self.defaults = common_params()
        self.sampling_rate = 1500
        
        
    def create_channel_headings(self, channels):
        headings = []
        for i in range(1, channels + 1):
            headings.append("channel_" + str(i))
        return headings
     
    def export_df(self):
        heading_names = self.create_channel_headings(channels = 21)
        raw_data = pd.read_csv(self.location, header = None, names = heading_names)
        time = pd.Series(data = (raw_data.index + 1)/self.sampling_rate , index=raw_data.index)
        time.name = "time"
        data_series = pd.concat([time, raw_data], axis = 1)
        
        return data_series

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        # data_series.iloc[0:limit, :].plot(x = "time", y = "channel_" + str(channel), figsize=(48, 4))
        data_series.plot(x = "time", y = "channel_" + str(channel))
        plt.show()
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = fft(data_series[ds_key].to_numpy())
        xf = fftfreq(N, 1/self.sampling_rate)
        return (xf, yf)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = rfft(data_series[ds_key].to_numpy())
        xf = rfftfreq(N, 1/self.sampling_rate)
        return (xf, yf)

    def plot_fft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_fft(channel = channel)
        yf_mag = np.abs(yf)
        # yf_shifted = fftshift(yf_mag)
        plt.plot(xf, yf_mag)
        plt.show()
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_rfft(channel = channel)
        plt.plot(xf, np.abs(yf))
        plt.show()
    
class TLA:
    defaults = common_params()
    
    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/tla_raw.csv"
        self.sampling_rate = 1500

    def create_channel_headings(self, channels):
        headings = []
        for i in range(1, channels + 1):
            headings.append("channel_" + str(i))
        return headings
    
    def export_df(self):
        heading_names = self.create_channel_headings(channels = 22)
        raw_data = pd.read_csv(self.location, header = None, names = heading_names)
        time = pd.Series(data = (raw_data.index + 1)/self.sampling_rate, index=raw_data.index)
        time.name = "time"
        data_series = pd.concat([time, raw_data], axis = 1)
        
        return data_series
        
    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        # data_series.iloc[0:limit, :].plot(x = "time", y = "channel_" + str(channel), figsize=(48, 4))
        data_series.plot(x = "time", y = "channel_" + str(channel))
        plt.show()
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = fft(data_series[ds_key].to_numpy())
        xf = fftfreq(N, 1/self.sampling_rate)
        return (xf, yf)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = rfft(data_series[ds_key].to_numpy())
        xf = rfftfreq(N, 1/self.sampling_rate)
        return (xf, yf)

    def plot_fft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_fft(channel = channel)
        yf_mag = np.abs(yf)
        # yf_shifted = fftshift(yf_mag)
        plt.plot(xf, yf_mag)
        plt.show()
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_rfft(channel = channel)
        plt.plot(xf, np.abs(yf))
        plt.show()

class HLA_North:
    defaults = common_params()    

    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/hla_n_raw.csv"
        self.sampling_rate = 3276.8 
        
    def create_channel_headings(self, channels):
        headings = []
        for i in range(1, channels + 1):
            headings.append("channel_" + str(i))
        return headings
    
    def export_df(self):
        heading_names = self.create_channel_headings(channels = 27)
        raw_data = pd.read_csv(self.location, header = None, names = heading_names)
        time = pd.Series(data = (raw_data.index + 1)/self.sampling_rate, index=raw_data.index)
        time.name = "time"
        data_series = pd.concat([time, raw_data], axis = 1)
        return data_series

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        # data_series.iloc[0:limit, :].plot(x = "time", y = "channel_" + str(channel), figsize=(48, 4))
        data_series.plot(x = "time", y = "channel_" + str(channel))
        plt.show()
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = fft(data_series[ds_key].to_numpy())
        xf = fftfreq(N, 1/self.sampling_rate)
        return (xf, yf)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = rfft(data_series[ds_key].to_numpy())
        xf = rfftfreq(N, 1/self.sampling_rate)
        return (xf, yf)

    def plot_fft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_fft(channel = channel)
        yf_mag = np.abs(yf)
        # yf_shifted = fftshift(yf_mag)
        plt.plot(xf, yf_mag)
        plt.show()
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_rfft(channel = channel)
        plt.plot(xf, np.abs(yf))
        plt.show()

class HLA_South:
    defaults = common_params()    

    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/hla_s_raw.csv"
        self.sampling_rate = 3276.8
    
    def create_channel_headings(self, channels):
        headings = []
        for i in range(1, channels + 1):
            headings.append("channel_" + str(i))
        return headings
    
    def export_df(self):
        heading_names = self.create_channel_headings(channels = 28)
        raw_data = pd.read_csv(self.location, header = None, names = heading_names)
        time = pd.Series(data = (raw_data.index + 1)/self.sampling_rate, index=raw_data.index)
        time.name = "time"
        data_series = pd.concat([time, raw_data], axis = 1)
        return data_series

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        # data_series.iloc[0:limit, :].plot(x = "time", y = "channel_" + str(channel), figsize=(48, 4))
        data_series.plot(x = "time", y = "channel_" + str(channel))
        plt.show()
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = fft(data_series[ds_key].to_numpy())
        xf = fftfreq(N, 1/self.sampling_rate)
        return (xf, yf)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        data_series = self.export_df()
        N = len(data_series.index)
        ds_key = "channel_" + str(channel)
        yf = rfft(data_series[ds_key].to_numpy())
        xf = rfftfreq(N, 1/self.sampling_rate)
        return (xf, yf)

    def plot_fft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_fft(channel = channel)
        yf_mag = np.abs(yf)
        # yf_shifted = fftshift(yf_mag)
        plt.plot(xf, yf_mag)
        plt.show()
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        xf, yf = self.calculate_rfft(channel = channel)
        plt.plot(xf, np.abs(yf))
        plt.show()

# if __name__ == "__main__":
#     print(__file__.split("Data")[0].replace("\\", "/"))