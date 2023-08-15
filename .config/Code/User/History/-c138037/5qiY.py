#!/usr/bin/env python3

from libqtile.command.client import InteractiveCommandClient
from time import sleep

c = InteractiveCommandClient()

while "Steam" not in c.group["tray"].info()["windows"]: # wait until steam exsists
    continue

sleep(10)

# reset the layout and make discord as big as possible
c.group["tray"].layout.reset()
c.group["tray"].layout.maximize() # maximize the manepane of the monadtall layout in the tray group
