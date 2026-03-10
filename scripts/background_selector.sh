#!/bin/zsh

backgrounds=(~/Pictures/background/*)

# Use the j parameter expantion flag to join the backgrounds array 
# into a single string with \n delimeters. Zsh only!!!
selected_bg=$(echo -e ${(j[\n])backgrounds} | rofi -dmenu)

# Rofi outputs the filepath directly so we can pull that
hyprctl hyprpaper wallpaper "DP-2, $selected_bg, cover"
hyprctl hyprpaper wallpaper "HDMI-A-1, $selected_bg, cover"

# Save the background
truncate -s 0 ~/.config/hypr/var-background.conf # Clear the file
echo "\$file = ${selected_bg}" >> ~/.config/hypr/var-background.conf # Add the variable
