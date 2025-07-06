#!/usr/bin/env python3.13
from libqtile.command.client import InteractiveCommandClient
from time import sleep

c = InteractiveCommandClient()

sleep(10)

# reset the layout and make discord as big as possible
c.group["tray"].setlayout("monadtall")
c.group["tray"].layout.reset()
c.group["tray"].layout.maximize()

# setup autio group
c.group["a/v"].setlayout("monadtall")
