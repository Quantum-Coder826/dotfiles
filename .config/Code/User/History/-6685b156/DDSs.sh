#!/bin/bash
# prompt that will ask to cancle, logout, reboot or shutdown

ans=$(zenity --question --title "shutdown" \
    --text "Shutdown: Are you shure you want to power off?" \
    --default-cancel \
    -icon-name "/usr/share/icons/Mint-Y-Dark/actions/48/system-shutdown.png" \
    --ok-label="shutdown" \
    --cancel-label="cancel")
rc=$?
echo "${rc}-${ans}"