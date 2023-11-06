import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, rfft, rfftfreq, fftshift

from Source.Core import System_Core
from Source.Common import common_params
               
class VLA:
    defaults = common_params()
    
    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/vla_raw.csv"
        self.sampling_rate = 1500   
        self.num_channels = 21   
        self.sys_name = "VLA"  
        self.system = System_Core(
            location = self.location, 
            sampling_rate = self.sampling_rate,
            num_channels = self.num_channels,
            system_name = self.sys_name
            )        
        
    def export_df(self):
        return self.system.export_df()

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        self.system.plot_time_series(channel = channel)
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_fft(channel = channel)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_rfft(channel = channel)

    def plot_fft(self, channel = defaults.default_plot_channel):
        self.system.plot_fft(channel = channel)
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        self.system.plot_rfft(channel = channel)
        
    def generate_spectrogram(self, channel = defaults.default_plot_channel):
        self.system.generate_spectrogram(channel = channel)
    
class TLA:
    defaults = common_params()
    
    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/tla_raw.csv"
        self.sampling_rate = 1500
        self.num_channels = 22
        self.sys_name = "TLA"
        self.system = System_Core(
            location = self.location, 
            sampling_rate = self.sampling_rate,
            num_channels = self.num_channels,
            system_name = self.sys_name
            )        
        
    def export_df(self):
        return self.system.export_df()

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        self.system.plot_time_series(channel = channel)
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_fft(channel = channel)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_rfft(channel = channel)

    def plot_fft(self, channel = defaults.default_plot_channel):
        self.system.plot_fft(channel = channel)
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        self.system.plot_rfft(channel = channel)

    def generate_spectrogram(self, channel = defaults.default_plot_channel):
        self.system.generate_spectrogram(channel = channel)

class HLA_North:
    defaults = common_params()    

    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/hla_n_raw.csv"
        self.sampling_rate = 3276.8 
        self.num_channels = 27
        self.sys_name = "HLA North"
        self.system = System_Core(
            location = self.location, 
            sampling_rate = self.sampling_rate,
            num_channels = self.num_channels,
            system_name = self.sys_name
            )           
        
    def export_df(self):
        return self.system.export_df()

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        self.system.plot_time_series(channel = channel)
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_fft(channel = channel)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_rfft(channel = channel)

    def plot_fft(self, channel = defaults.default_plot_channel):
        self.system.plot_fft(channel = channel)
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        self.system.plot_rfft(channel = channel)

    def generate_spectrogram(self, channel = defaults.default_plot_channel):
        self.system.generate_spectrogram(channel = channel)

class HLA_South:
    defaults = common_params()    

    def __init__(self) -> None:
        self.curr_loc = __file__.split("System")[0].replace("\\", "/")
        self.location = self.curr_loc + "excel_export/hla_s_raw.csv"
        self.sampling_rate = 3276.8
        self.num_channels = 28
        self.sys_name = "HLA South"
        self.system = System_Core(
            location = self.location, 
            sampling_rate = self.sampling_rate,
            num_channels = self.num_channels,
            system_name = self.sys_name
            )    
    def export_df(self):
        return self.system.export_df()

    def plot_time_series(self, limit = defaults.default_point_limit, channel = defaults.default_plot_channel):
        self.system.plot_time_series(channel = channel)
        
    def calculate_fft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_fft(channel = channel)
    
    def calculate_rfft(self, channel = defaults.default_plot_channel):
        return self.system.calculate_rfft(channel = channel)

    def plot_fft(self, channel = defaults.default_plot_channel):
        self.system.plot_fft(channel = channel)
    
    def plot_rfft(self, channel = defaults.default_plot_channel):
        self.system.plot_rfft(channel = channel)

    def generate_spectrogram(self, channel = defaults.default_plot_channel):
        self.system.generate_spectrogram(channel = channel)
# if __name__ == "__main__":
#     print(__file__.split("Data")[0].replace("\\", "/"))