#!/usr/bin/env python3
from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()

class Mode:
    def __init__(self):
        self.mode_index = 0
        self.mode_list = ["nav", "size", "move"]