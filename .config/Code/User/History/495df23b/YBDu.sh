#!/bin/bash
# prompt that will ask to cancle, or power off reboot the system

ans=$(echo -e "cancel\nreboot" | rofi -dmenu -format i:s)

case "${ans:0:1}" in
    0) exit;;
    1) systemctl reboot;;
esac