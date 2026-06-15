#!/bin/bash

amd-smi metric --json | jq --unbuffered --compact-output '.gpu_data[0] | {text: "󰾲\(.usage.gfx_activity.value)󱉸", 
tooltip: "󰔏 \(.temperature.hotspot.value)󰔄\r󰈐 \(.fan.usage.value)󰏰\r󱩗 \(.power.socket_power.value)w"}' 

