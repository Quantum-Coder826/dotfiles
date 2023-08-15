#!/bin/bash
# prompt that will ask to cancle, or power off reboot the system

ans=$(echo -e "cancel\nreboot" | rofi -dmenu -format i:s)

case "${ans:0:1}" in
    0) exit;;
    1) systemctl reboot;;
esac



ans=$(zenity --question --title "reboot" \
    --text "Shutdown: Are you shure you want to restart?" \
    --default-cancel \
    --ok-label="reboot" \
    --cancel-label="cancel")
rc=$?

if [ $rc = 0 ]; then
    systemctl reboot
else 
    exit
fi