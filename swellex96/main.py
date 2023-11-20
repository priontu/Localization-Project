import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

# if __name__ == "__main__":
#     # vla_raw = pd.read_csv("excel_export/tla_raw.csv", header = ("channel_1", "channel_2", "channel_3", "channel_4", "channel_5", "channel_6", "channel_7", "channel_8", "channel_9", "channel_10", "channel_11", "channel_12", "channel_13", "channel_14", "channel_15", "channel_16", "channel_17", "channel_18", "channel_19", "channel_20", "channel_21"))
#     vla_raw = pd.read_csv("excel_export/vla_raw.csv", header = None, names = ("channel_1", "channel_2", "channel_3", "channel_4", "channel_5", "channel_6", "channel_7", "channel_8", "channel_9", "channel_10", "channel_11", "channel_12", "channel_13", "channel_14", "channel_15", "channel_16", "channel_17", "channel_18", "channel_19", "channel_20", "channel_21"))
    
#     time = pd.Series(data = (vla_raw.index + 1)/1500, index=vla_raw.index)
#     time.name = "time"
    
#     vla_series = pd.concat([time, vla_raw], axis = 1)
    
#     # plt.figure()
    
#     vla_series.iloc[0:2000000, 0:2].plot(x = "time", y = "channel_1")
#     plt.show()
    # # print(vla_series)
    
    # print(vla_series.iloc[0:100, 0:10])
    # print(vla_series)
    
from Source.System import VLA, TLA, HLA_North, HLA_South

# VLA().plot()
VLA().plot_rfft_phase(channel = 10)