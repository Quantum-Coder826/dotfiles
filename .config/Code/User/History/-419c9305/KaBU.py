#!/usr/bin/env python3

from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()

currentScreenIndex = c.screen.info()["index"]


