#!/bin/bash
# prompt that will ask to cancle, logout, reboot or shutdown

ans=$(zenity --question --title 'Choose!' \
    --text 'logout' \
    --default-cancel \
    --ok-label="shutdown" \
    --cancel-label="cancle")
rc=$?
echo "${rc}-${ans}"