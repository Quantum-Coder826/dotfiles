#!/bin/bash

ans=$(echo -e " monitor\n window\n region\n active\n cancel" | rofi -dmenu -format i:s)

case "${ans:0:1}" in
    0) hyprshot -s -m output;;
    1) hyprshot -s -m window;;
    2) hyprshot -s -m region;;
    3) hyprshot -s -m active;;
    4) exit;;
esac