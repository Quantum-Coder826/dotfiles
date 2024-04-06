#!/bin/bash

mountpoint -q /media/berend/smb && notify-send -i info -t 1500 "SMB already mounted" && exit
echo "Enter root password to mount /media/berend/smb"
sudo -k -p "Password: " mount /media/berend/smb || notify-send -i error "Failed to mount /media/berend/smb" && exit
notify-send -i samba -t 1500 "Sucssfuly mounted /media/berend/smb"
exit
