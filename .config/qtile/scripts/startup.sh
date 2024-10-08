#!/bin/bash

# system services
(/usr/lib/x86_64-linux-gnu/libexec/org_kde_powerdevil &) # power daemon
(/usr/bin/lxqt-policykit-agent &) # polkit daemon
(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=qpwgraph --file-forwarding org.rncbc.qpwgraph &)
(easyeffects &)
(greenclip daemon &)
#(/home/qbyte/.config/qtile/scripts/bin/python3 /home/qbyte/.config/qtile/scripts/utils.py &)

# my startup apps
(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=com.discordapp.Discord com.discordapp.Discord &) # add --start-minimized when need to start in tray
(steam &)
