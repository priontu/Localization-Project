function [xf, yf] = generate_fft_spectrum(selected_data, Fs)

num_points = height(selected_data);

% selected_data = data_table{:, selected_channel};
dc_removed = selected_data - mean(selected_data);
Y_complex = fft(dc_removed);
Y_mag = abs(Y_complex);
Y_shifted = fftshift(Y_mag);
freq_spread = (Fs/num_points).*(-(num_points/2):(num_points/2 - 1));

xf = freq_spread;
yf = Y_shifted;