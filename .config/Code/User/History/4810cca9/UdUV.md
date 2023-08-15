# mcService
A simple service I wrote to run minecraft java servers under a linux systemd service

# installation
You can manually install or use the install script. Have fun

## preparations
check if you have `screen` installed, if it isn't pleas install the screen package by running:
```bash
sudo apt install screen
```

## automatic installation script
For automatic installation copy the following line and run it in the terminal.
```bash
wget -O - https://raw.githubusercontent.com/Quantum-Coder826/mcService/master/installer.sh | tr -d '\r' | bash
```
>**note**
> The install script is kinda dumb so it might fail.

## manual installation
- Create the following folder if it does not exist: `~/.config/systemd/user/`
- Copy/download the `mc@.service` file to that folder.
- Create a `minecraft` folder in your home directory.

# How to use

## Adding a server
Adding servers is easy create a sub-dir in the `~/minecraft` folder. Inside the sub-dir you can install your sever. Ensure the folder contains a `run.sh` and it is marked as executable (coloured <span style="color:green">green</span> when using the `ls` command in bash)
Most servers or modpacks will contain one just make ik executable using the `chmod +x run.sh` command.
After installing your server the tree listing should look something like this:
```
user@server ~/minecraft$ tree -dL 1 ~/minecraft/
/home/user/minecraft/
|-- Create
|-- MechanicalMastery-1.3.0
|   |-- banned-ips.json
|   |-- banned-players.json
|   |-- config
|   |-- defaultconfigs
|   |-- eula.txt
|   |-- icon.png
|   |-- kubejs
|   |-- libraries
|   |-- local
|   |-- logs
|   |-- mods
|   |-- ops.json
|   |-- packmenu
|   |-- patchouli_books
|   |-- quests_structures
|   |-- rhino.local.properties
|   |-- run.sh
|   |-- server.properties
|   |-- skyblock_exports
|   |-- user_jvm_args.txt
|   |-- usercache.json
|   |-- usernamecache.json
|   |-- whitelist.json
|   `-- world
|-- architect
|-- createTogether
|-- encrypted
|-- expert
`-- more

7 directories
```

## Running the service
To run the server you need to only run two commands:

### Enabling the service
Telling systemd that it should autostart your server.
This is optional but it is useful, if the minecraft crashes systemd will it restart for you and the server will automatically start after the machine is booted or restarted.
```bash
systemctl --user enable mc@<server-name>
```
`<server-name>` is the name of a sub-dir in `~/minecraft` where you will be running a server.

### Starting the server
This command will actually start the server so you will need it.
```bash
systemctl --user start mc@<server-name>
```
`<server-name>` is the name of a sub-dir in `~/minecraft` where you will be running a server.

The service will open a `screen` session in the background so check using `screen -ls` and looking for a session named `mc_<server-name>`.

# Connecting with a server
The servers are spawned in a screen session you can list all active session using `screen -ls` the result should look something like:
```bash
user@server ~/minecraft$ screen -ls
There is a screen on:
        5983.mc_MechanicalMastery-1.3.0 (05/22/24 00:37:12)     (Detached)
1 Socket in /run/screen/S-user.
```
The name formatting is `mc_<server-name>

Screen is used to access the server terminal, you can run multiple servers but the naming convention for screen will stay the same, os running multiple servers with the same name might lead to problems differentiating in screen session.

## How do i use screen?
Here is a [link](https://wiki.archlinux.org/title/GNU_Screen) to the archwiki.