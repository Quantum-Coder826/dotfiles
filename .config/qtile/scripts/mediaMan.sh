#!/bin/bash

ans=$(echo -e "0) ToDo:make it work\n1) Cancel" | rofi -dmenu -format i:s -p 'mediaMan')

case "${ans:0:1}" in
    0) exit;;
    1) exit;;
esac

