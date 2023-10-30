function generate_fft_spectrum_plot(system_name, selected_channel, freq_spread, Y_shifted)

figure;
indices = (freq_spread>0) & (freq_spread < 600);
plot(freq_spread(indices), Y_shifted(indices));
xlabel("frequency/Hz");
ylabel("Magnitude");
title((strcat("Frequency Domain Display, ", system_name, " Channel: ", int2str(selected_channel))));
hold on;
grid on;
