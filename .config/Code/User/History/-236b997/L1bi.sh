#!/bin/bash

# varables used for color
GREEN="\e[0;32m"
YELLOW="\e[0;33m"
BLUE="\e[0;34m"
ENDCOLOR="\e[0m"

mkdir -p ~/.config/systemd/user/
echo -e "${BLUE}Downloading service file${ENDCOLOR}"
wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

echo -e "${BLUE}Creating server folder${ENDCOLOR}"
mkdir -p ~/minecraft/


echo "KillUserProcesses=no" >> /etc/systemd/logind.conf

systemctl --user daemon-reload
systemctl restart systemd-logind
echo -e "${GREEN}Instalation is done.\nSee: https://github.com/Quantum-Coder826/mcService for the docs. ${ENDCOLOR}"
exit 0
