#!/usr/bin/env python3
from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()

#general use vars
mode_index = 0
mode_list = ["nav", "size", "move"]

def next_mode():    
    if mode_index > len(mode_list): # ensure we loop (eg do not index out_of_bounds)
        mode_index = 0
    
    # update the mode_indicator in the bar
    if mode_index == 0:
        c.widget["mode_indicator"].update("") #we do not show mode 0
        return mode_index
    else:
        c.widget["mode_indicator"].update(mode_list[mode_index]) #show the mode
        return mode_index

next_mode()