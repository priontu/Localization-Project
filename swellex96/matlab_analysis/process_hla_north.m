function process_hla_north(p1, npi, selected_channel)

% p1 is starting point.
% npi is number of points to load.

default_selected_channel = 1; % Default Channel being studied.
default_p1 = 1;
default_npi = 0;

num_channels = 27;
Fs = 3276.8;  % sampling frequency

if ~exist('p1', 'var')
    p1 = default_p1;
end

if ~exist('npi', 'var')
    npi = default_npi;
end

if ~exist('selected_channel', 'var')
    selected_channel = default_selected_channel;    % Default Channel being studied.
end


data_path = '../data/J1312340.hla.north.sio';
channels = 1:num_channels;

metadata = {data_path, p1, npi, channels};
raw_data = sioread(metadata{:});

[nr, nc] = size(raw_data);
num_points = nr;

names = generate_channel_names(num_channels);
data_table = array2table(raw_data, "VariableNames", names);
timeline = (0:(num_points - 1))./Fs;

figure(5);
plot(timeline, data_table{:, selected_channel});
title(strcat('Time Domain Display, HLA North Channel: ', int2str(selected_channel)));
xlabel("time/s");
ylabel("Magnitude");
hold on;
grid on;

Y = fft(data_table{:, selected_channel});
freq_spread = (Fs/num_points)*(-(num_points/2):(num_points/2 - 1));

figure(6);
plot(freq_spread, abs(Y));
xlabel("frequency/Hz");
ylabel("Magnitude");
title(strcat('Frequency Domain Display, HLA North Channel: ', int2str(selected_channel)));
hold on;
grid on;






