#!/bin/bash
# prompt that will ask to cancle, or power off reboot the system

ans=$(echo -e "cancel\n1) reboot\n2) reboot to UEFI" | rofi -dmenu -format i:s)

case "${ans:0:1}" in
    0) exit;;
    1) systemctl reboot;;
    2) systemctl reboot --firmware-setup;;
esac