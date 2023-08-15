#!/bin/bash

# varables used for color
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[e34m"
ENDCOLOR="\e[0m"

# check root
if [$USER == "root"]; then
    echo -e "${YELLOW}This file does not need to be run as root. Exiting${ENDCOLOR}"
    exit 1
fi

#check for screen
if ![dpkg -s screen > /dev/null]; then
    echo -e "${YELLOW}The pa${ENDCOLOR}"
    

mkdir -p ~/.config/systemd/user/
echo -e "${BLUE}Downloading service file${ENDCOLOR}"
wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

mkdir -p ~/minecraft/
echo -e "${GREEN}Install compleate${ENDCOLOR}"
echo "Minecraft servers can now be installed 