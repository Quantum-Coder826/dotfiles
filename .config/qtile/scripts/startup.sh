#!/bin/bash

# system config
## disable screen saver, brancker & power managment - this is a pc not a laptop
xset s off
xset x noblank
xset -dmps

# system apps
(amixer -c2 sset 'Input Source',0 'Line' &)
(/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &)
(env GTK_THEME=Adwaita:dark /usr/bin/flatpak run --branch=stable --arch=x86_64 --command=easyeffects com.github.wwmm.easyeffects &)
(/usr/bin/qpwgraph ~/Documents/patchbay/Headset.qpwgraph -ax &)
(/home/berend/.local/bin/greenclip daemon &)

# my startup apps
(flatpak run com.valvesoftware.Steam &)
(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=com.discordapp.Discord com.discordapp.Discord &) # add --start-minimized when need to start in tray

