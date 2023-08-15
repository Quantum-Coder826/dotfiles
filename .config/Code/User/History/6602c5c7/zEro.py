#!/usr/bin/env python3
#!/usr/bin/env python3
import logging, sys
from libqtile.command.client import InteractiveCommandClient
from time import sleep

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG) # set the logging level.

c = InteractiveCommandClient()

#general use vars
mode_index = 0
mode_list = ["nav", "size", "move"]

def next_mode():
    mode_index += 1
    if mode_index > len(mode_list): # ensure we loop ()
        mode_index = 0