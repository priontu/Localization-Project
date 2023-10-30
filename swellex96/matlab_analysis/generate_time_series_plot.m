function generate_time_series_plot(system_name, selected_channel, selected_data, timeline)

figure;
plot(timeline, selected_data);
title((strcat("Time Domain Display, ", system_name," Channel: ", int2str(selected_channel))));
xlabel("time/s");
ylabel("Magnitude");
hold on;
grid on;