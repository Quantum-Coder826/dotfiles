#!/usr/bin/env python3.11
from subprocess import Popen, check_output, PIPE
from shlex import split
import json

def findNodeByDescription(description):
    dump = json.loads(check_output(split("pw-dump")))

    for ent in enumerate(dump):
        try:
            if ent[1]['type'] == 'PipeWire:Interface:Node': 
                if ent[1]['info']['props']['media.class'] == 'Audio/Sink':
                    if description in ent[1]['info']['props']['node.description']:
                        return(ent)
        except:
            continue

def rofiDemenuChoicePrompt(dmenuStr = "Cancel"):
    echoProcess = Popen(split("echo -e '" + dmenuStr + "'"), stdout=PIPE)
    rofi = check_output(split("rofi -dmenu -format i:s -p 'mediaMan'"), stdin=echoProcess.stdout)
    return int(chr(rofi[0]))

result = rofiDemenuChoicePrompt(str(check_output(split("playerctl metadata --format 'Now playing: {{ artist }} - {{ title }}'")).decode("utf-8")) + 
                                "󰐎 Play/Pause\n󰒭 Next\n󰒮 Previous\n󱡫 Default ouput 󰍟\n󰅖 Close")

if result == 0:
    exit()
if result == 1:
    Popen(split("playerctl play-pause"))
if result == 2:
    Popen(split("playerctl next"))
if result == 3:
    Popen(split("playerctl previous"))
if result == 4:
    result = rofiDemenuChoicePrompt("󰋎 Headset\n󰓃 Speaker\n󰅖 Close")
    if result == 0:
        node = findNodeByDescription("Headset")
        Popen(split("wpctl set-default " + str(node[1]['id'])))
        exit()
    if result == 1:
        node = findNodeByDescription("Speakers")
        Popen(split("wpctl set-default " + str(node[1]['id'])))
        exit()
    if result == 2:
        exit()
if result == 5:
    exit()
