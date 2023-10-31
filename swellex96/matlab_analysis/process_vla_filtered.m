function process_vla_filtered(p1, npi, selected_channel, threshold)

% p1 is starting point.
% npi is number of points to load.
system_name = "VLA";
default_selected_channel = 1; % Channel being studied.

default_p1 = 1;
default_npi = 0;

if ~exist('p1', 'var')
    p1 = default_p1;
end

if ~exist('npi', 'var')
    npi = default_npi;
end

if ~exist('selected_channel', 'var')
    selected_channel = default_selected_channel;
end

if ~exist('threshold', 'var')
    threshold = -Inf;
end

Fs = 1500;  % sampling frequency

data_path = '../data/J1312315.vla.21els.sio';
channels = 1:21;
metadata = {data_path, p1, npi, channels};

raw_data = sioread(metadata{:});

[nr, nc] = size(raw_data);
num_points = nr;

names = generate_channel_names(21);
data_table = array2table(raw_data, "VariableNames", names);
timeline = (0:(num_points - 1))./(Fs);
selected_data = data_table{:, selected_channel};

selected_data = bandpass(selected_data, [40, 500], Fs);

generate_time_series_plot(system_name, selected_channel, selected_data, timeline);

[freq_spread, Y_shifted] = generate_fft_spectrum(selected_data, Fs);

generate_fft_spectrum_plot(system_name, selected_channel, freq_spread, Y_shifted);

generate_spectrogram(system_name, selected_channel, selected_data, Fs, threshold);

% barlett_win = barlett(num_points);
% Ndft = 4096

