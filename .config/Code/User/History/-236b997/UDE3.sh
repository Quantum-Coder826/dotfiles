#!/bin/bash

# varables used for color
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[e34m"
ENDCOLOR="\e[0m"

if [$USER == "root"]; then
    echo -e "${YELLOW}This file does not need to be run as root. Exiting${ENDCOLOR}"
    exit 1
fi

mkdir -p ~/.config/systemd/user/
echo -e "${BLUE}Downloading service file${ENDCOLOR}"
wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

mkdir 