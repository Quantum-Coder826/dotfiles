# mcService
A simple service I wrote to run minecraft java servers under a linux systemd service

# installation

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
### 
telling systemd that it should autostart your server.
This is optional but it is useful that if the minecraft crashes that it will restart itself and that your server will automatically start after the machine it is running on has booted up.
```bash
systemctl --user enable mc@<server-name>
```
`<server-name>` is the name of a sub-dir in `~/minecraft` where you will be running a server.
