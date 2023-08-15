#!/bin/bash

# varables used for color
GREEN="\e[32m"
YELLOW="\e[33m"
ENDCOLOR="\e[0m"

if [$USER == "root"]; then
    echo "This file does not need to be run as root. Exiting..."
    exit 1
fi

mkdir -p ~/.config/systemd/user/
echo -e "${YELLOW}Downloading service file${ENDCOLOR}"
wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

