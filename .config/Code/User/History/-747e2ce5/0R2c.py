#!/usr/bin/env python3
from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()

class Mode:
    def __init__(self):
        self.mode_index = 0
        self.mode_list = ["nav", "size", "move"]
        c.widget["mode_indicator"].update("")
        
    
    def next(self):
        self.mode_index += 1
        if 
        c.widget["mode_indicator"].update(str(self.mode_index))
        return True