#!/bin/bash
# prompt that will ask to cancle, or power off the system

ans=$(echo -e "cancel\nshutdown" | rofi -dmenu -format i:s)

case "${ans:0:1}" in
    0) systemctl poweroff;;
    1) exit;;
esac


# ans=$(zenity --question --title "shutdown" \
#    --text "Shutdown: Are you shure you want to power off?" \
#    --default-cancel \
#    --ok-label="shutdown" \
#    --cancel-label="cancel")
#rc=$?
#
#if [ $rc = 0 ]; then
#    systemctl poweroff
#else 
#    exit
#fi