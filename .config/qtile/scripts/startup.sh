#!/bin/bash

# xrander
xrandr --output HDMI-0 --primary --auto
xrandr --output DVI-D-0 --left-of HDMI-0

# system services
(/usr/lib/polkit-kde-authentication-agent-1 &)
(XDG_MENU_PREFIX=arch- kbuildsycoca6 &)

#(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=qpwgraph --file-forwarding org.rncbc.qpwgraph &)
(/usr/bin/helvum &)
(com.github.wwmm.easyeffects &)
(/home/qbyte/.local/bin/greenclip daemon &)
#(/home/qbyte/.config/qtile/scripts/bin/python3 /home/qbyte/.config/qtile/scripts/utils.py &)
(/bin/bash /home/qbyte/.config/qtile/scripts/net_up.sh &)

# my startup apps
(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=com.discordapp.Discord com.discordapp.Discord &) # add --start-minimized when need to start in tray
(steam &)
