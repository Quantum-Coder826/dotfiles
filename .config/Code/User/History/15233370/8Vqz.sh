#!/bin/bash

ans=$(echo -e "obs\nobs camera stream\ncancel" | rofi -dmenu -format i:s)

case "${ans:0:1}" in
    0) obs;;
    1) obs --startvirtualcam
    2) systemctl reboot --firmware-setup;;
esac