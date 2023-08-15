#!/usr/bin/env python3

from libqtile.command.client import InteractiveCommandClient
from time import sleep

c = InteractiveCommandClient()

print(c.group["tray"].info()["windows"])
c.group["tray"].layout.maximize() # maximize the manepane of the monadtall layout in the tray group
