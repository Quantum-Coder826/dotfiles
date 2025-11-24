#!/usr/bin/env python3.13
from subprocess import Popen, check_output, PIPE
from shlex import split
from json import loads

output = {"text": "", "tooltip": ""}

metrics = loads(check_output(split("amd-smi metric --json")))

##########
## text ##
##########

# gfx usage
output["text"] += "󰾲 " + str(metrics[0]['usage']['gfx_activity']['value']) + "󱉸"

#############
## tooltip ##
#############

# amd-smi provides vram usage & total as megabytes so a percentage needs to be calculated 
mem_total = metrics[0]['mem_usage']['total_vram']['value']
mem_used = metrics[0]['mem_usage']['used_vram']['value']

mem_percentage = round((mem_used / mem_total) * 100, 1)
output["tooltip"] += "󰍛 " + str(mem_percentage) + "󱉸"

# temperatue
output["tooltip"] += "\n󱃃 " + str(metrics[0]['temperature']['hotspot']['value']) + "󰔄"

# fan
output["tooltip"] += "\n󰈐 " + str(metrics[0]['fan']['usage']['value']) + "󱉸"

# power
output["tooltip"] += "\n󱩗 " + str(metrics[0]['power']['socket_power']['value']) + "W"
