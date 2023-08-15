#!/bin/bash

(/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=discord com.discordapp.Discord --start-minimized &)
(sh -c 'STEAM_FRAME_FORCE_CLOSE=1 steam -silent %U' &)
exit