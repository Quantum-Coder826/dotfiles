#!/usr/bin/env python3
#!/usr/bin/env python3
import logging, sys
from libqtile.command.client import InteractiveCommandClient
from time import sleep

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG) # set the logging level.

c = InteractiveCommandClient()

#general use vars
global mode_index = 0
global mode_list = ["nav", "size", "move"]

def next_mode():
    mode_index += 1
    if mode_index > len(mode_list): # ensure we loop (eg do not index out_of_bounds)
        mode_index = 0
    
    # update the mode_indicator in the bar
    if mode_index == 0:
        c.widget["mode_indicator"].update("") #we do not show mode 0
        return True
    else:
        c.widget["mode_indicator"].update(mode_list[mode_index]) #show the mode
