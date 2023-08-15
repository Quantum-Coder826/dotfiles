#!/bin/bash

ans=$(echo -e "cancel\nreboot\nreboot to UEFI" | rofi -dmenu -format i:s)