#!/bin/bash

# system apps
(/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &)
(env GTK_THEME=Adwaita:dark /usr/bin/flatpak run --branch=stable --arch=x86_64 --command=easyeffects-wrapper com.github.wwmm.easyeffects &)

# my startup apps
(sh -c 'STEAM_FRAME_FORCE_CLOSE=1 steam %U' &) # -silent to start to tray
(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=discord com.discordapp.Discord &) # add --start-minimized when need to start in tray