#!/bin/bash
sleep 1

# wlr-randr
wlr-randr --output DP-2 --mode 1920x1080@74.973000
wlr-randr --output HDMI-A-1 --mode 1920x1080@60.000000 --left-of HDMI-A-1

# system services
(/usr/lib/polkit-kde-authentication-agent-1 &)
(XDG_MENU_PREFIX=arch- kbuildsycoca6 &)

(/usr/bin/helvum &)
(com.github.wwmm.easyeffects &)
(wl-paste --watch cliphist store &)
(/bin/bash /home/qbyte/.config/qtile/scripts/net_up.sh &)
(../bin/python3.11 ./utils.py)

# my startup apps
(com.discordapp.Discord &) # add --start-minimized when need to start in tray
(steam &)
