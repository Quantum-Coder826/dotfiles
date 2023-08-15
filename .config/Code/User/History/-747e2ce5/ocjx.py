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
        if self.mode_index > len(self.mode_list) - 1: # check length to prefent a index_out_of_bounds error
            self.mode_index = 0
        
        if self.mode_index == 0:
            c.widget["mode_indicator"].update("")
            return True
        else:
            c.widget["mode_indicator"].update(self.mode_list[self.mode_index])
            return True