#!/bin/bash

if [$USER == "root"]; then
    echo "This file does not need to be run as root. Exiting..."
    exit 1
fi

mkdir -p ~/.config/systemd/user/
echo -e "${}
wget -O ~/.config/systemd/user/mc@.service https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/mc%40.service

