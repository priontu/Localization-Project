function x = generate_channel_names(num_channels)

channel_names = cell(1, num_channels);

for ii = 1:num_channels
    name = strcat("channel_", int2str(ii));
    char_name = convertStringsToChars(name);
    channel_names{1, ii} = char_name;
end

x = channel_names;