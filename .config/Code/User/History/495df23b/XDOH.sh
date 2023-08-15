#!/bin/bash
# prompt that will ask to cancle, or power off reboot the system

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