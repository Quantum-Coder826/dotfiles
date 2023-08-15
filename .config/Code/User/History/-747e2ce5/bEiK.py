#!/usr/bin/env python3
from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()

#general use vars
mode_index = 1
mode_list = ["nav", "size", "move"]

def next_mode():
    # pull the vars
    global mode_index
    global mode_list
    
    mode_index = mode_index + 1
    if mode_index > len(mode_list): # ensure we loop (eg do not index out_of_bounds)
        mode_index = 0
    
    # update the mode_indicator in the bar
    if mode_index == 0:
        c.widget["mode_indicator"].update("") #we do not show mode 0
        return True
    else:
        c.widget["mode_indicator"].update(mode_list[2]) #show the mode

next_mode()