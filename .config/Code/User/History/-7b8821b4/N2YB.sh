#!/bin/bash

(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=discord com.discordapp.Discord &) # add --start-minimized when need to start in tray
(sh -c 'STEAM_FRAME_FORCE_CLOSE=1 steam -silent %U' &)