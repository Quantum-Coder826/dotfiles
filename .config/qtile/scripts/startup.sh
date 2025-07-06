#!/bin/bash

# xrander
xrandr --output HDMI-0 --primary --auto
xrandr --output DVI-D-0 --left-of HDMI-0

# system services
(/usr/lib/polkit-kde-authentication-agent-1 &)
(XDG_MENU_PREFIX=arch- kbuildsycoca6 &)

(/usr/bin/helvum &)
(com.github.wwmm.easyeffects &)
(/home/qbyte/.local/bin/greenclip daemon &)
(/bin/bash /home/qbyte/.config/qtile/scripts/net_up.sh &)

# my startup apps
(/usr/bin/discord &) # add --start-minimized when need to start in tray
(steam &)
