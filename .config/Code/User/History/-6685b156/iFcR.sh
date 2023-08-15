#!/bin/bash
# prompt that will ask to cancle, logout, reboot or shutdown

ans=$(zenity --question --title "shutdown" \
    --text "Shutdown: Are you shure you want to power off?" \
    --default-cancel \
    --ok-label="shutdown" \
    --cancel-label="cancel")
rc=$?
echo "${rc}-${ans}"