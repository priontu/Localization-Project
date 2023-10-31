function process_hla_south(p1, npi, selected_channel, threshold)

% p1 is starting point.
% npi is number of points to load.

system_name = "HLA South";

default_selected_channel = 1; % Channel being studied.
default_p1 = 1;
default_npi = 0;

num_channels = 28;
Fs = 3276.8;  % sampling frequency

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

data_path = '../data/J1312340.hla.south.sio';
channels = 1:num_channels;

metadata = {data_path, p1, npi, channels};
raw_data = sioread(metadata{:});

[nr, nc] = size(raw_data);
num_points = nr;

names = generate_channel_names(num_channels);
data_table = array2table(raw_data, "VariableNames", names);
timeline = (0:(num_points - 1))./Fs;

selected_data = data_table{:, selected_channel};

generate_time_series_plot(system_name, selected_channel, selected_data, timeline);

[freq_spread, Y_shifted] = generate_fft_spectrum(selected_data, Fs);

generate_fft_spectrum_plot(system_name, selected_channel, freq_spread, Y_shifted);

generate_spectrogram(system_name, selected_channel, selected_data, Fs, threshold);


% figure(7);
% plot(timeline, data_table{:, selected_channel});
% title(strcat('Time Domain Display, HLA South Channel: ', int2str(selected_channel)));
% xlabel("time/s");
% ylabel("Magnitude");
% hold on;
% grid on;
% 
% Y_complex = fft(data_table{:, selected_channel});
% Y_mag = abs(Y_complex);
% Y_shifted = fftshift(Y_mag);
% freq_spread = (Fs/num_points)*(-(num_points/2):(num_points/2 - 1));
% 
% figure(8);
% plot(freq_spread, Y_shifted);
% xlabel("frequency/Hz");
% ylabel("Magnitude");
% title(strcat('Frequency Domain Display, HLA South Channel: ', int2str(selected_channel)));
% hold on;
% grid on;

% figure(12);
% nsc = floor(num_points/1500);
% nov = floor(nsc/2);
% nff = max(256,2^nextpow2(nsc));
% 
% spectrogram(data_table{:, selected_channel}, hamming(nsc), nov, nff, Fs);
% title((strcat("Spectrogram, HLA South Channel: ", int2str(selected_channel))));
% hold on;

