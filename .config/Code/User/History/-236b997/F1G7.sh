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
if ![dpkg -s hjklj; > /dev/null]; then
    echo -e "${YELLOW}The screen package is not installed\n Please run 'sudo apt install screen' to install the package and then re-run the installer.${ENDCOLOR}"
    exit 1

mkdir -p ~/.config/systemd/user/
echo -e "${BLUE}Downloading service file${ENDCOLOR}"
wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

mkdir -p ~/minecraft/
echo -e "${GREEN}Instalation is done.${ENDCOLOR}"
exit 0