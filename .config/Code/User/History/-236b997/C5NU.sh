#!/bin/bash

# varables used for color
GREEN="\e[0;32m"
YELLOW="\e[0;33m"
BLUE="\e[0;34m"
ENDCOLOR="\e[0m"

# check root
if [ $USER == "root" ]; then
    echo -e "${YELLOW}This file does not need to be run as root. Exiting${ENDCOLOR}"
    exit 1
fi

#check for screen
if [ dpkg -s screen > /dev/null ]; then
    mkdir -p ~/.config/systemd/user/
    echo -e "${BLUE}Downloading service file${ENDCOLOR}"
    wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

    echo -e "${BLUE}Creating server folder${ENDCOLOR}"
    mkdir -p ~/minecraft/

    echo -e "${GREEN}Instalation is done.${ENDCOLOR}"
    exit 0
else
    echo -e "${YELLOW}The screen package is not installed\n Please run 'sudo apt install screen' to install the package and then re-run the installer.${ENDCOLOR}"
    exit 1
fi
