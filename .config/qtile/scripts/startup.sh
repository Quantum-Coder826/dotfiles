#!/bin/bash

## Screen setup for xorg
xrandr --output HDMI-0 --mode 1920x1080 --rate 75 --primary
xrandr --output DVI-D-0 --mode 1920x1080 --left-of HDMI-0

# system services
(/usr/lib/x86_64-linux-gnu/libexec/org_kde_powerdevil &) # power daemon
(/usr/bin/lxqt-policykit-agent &) # polkit daemon
(qpwgraph &)
(easyeffects &)
(greenclip daemon &)
#(/home/qbyte/.config/qtile/scripts/bin/python3 /home/qbyte/.config/qtile/scripts/utils.py &)

# my startup apps
(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=com.discordapp.Discord com.discordapp.Discord &) # add --start-minimized when need to start in tray
(steam &)
