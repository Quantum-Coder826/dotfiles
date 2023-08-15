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
if [dpkg -s screen > /dev/null]; then
    echo -e "${YELLOW}The screen package is not installed\n Please run 'sudo apt install screen' to install the package and then re-run the installer.${ENDCOLOR}"
    exit 1
fi

