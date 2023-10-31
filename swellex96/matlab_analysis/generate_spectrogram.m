function generate_spectrogram(system_name, selected_channel, selected_data, Fs, threshold)

% fprintf("num_points: %d", num_points);
num_points = height(selected_data);

% selected_data = data_table{:, selected_channel};
dc_removed = selected_data - mean(selected_data);

figure;
nsc = floor(num_points/(1500));
nov = floor(nsc/2);
nff = max(256,2^nextpow2(nsc));

fprintf("nsc: %f \n", nsc);
fprintf("nov: %f \n", nov);

spectrogram(dc_removed, hamming(nsc), nov, nff, Fs, "power", "MinThreshold", threshold);
title((strcat("Spectrogram, ", system_name, " Channel: ", int2str(selected_channel))));
colormap default;
hold on;