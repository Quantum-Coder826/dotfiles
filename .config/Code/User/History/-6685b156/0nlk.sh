#!/bin/bash
# prompt that will ask to cancle, logout, reboot or shutdown

while true; do
    ans=$(zenity --question --title 'Choose!' \
        --text 'logout' \
        --default-cancel \
        --ok-label="shutdown")
    rc=$?
    echo "${rc}-${ans}"
done