#!/usr/bin/env python3

from libqtile.command.client import InteractiveCommandClient
from mss.linux import MSS as mss
from datetime import datetime
from sys import argv

c = InteractiveCommandClient()

time = datetime.now()

# this variable is used to set wich screen is captured
# -1 for all screens
# 1 for main monitor
# 2 for secondairy

if len(argv) <= 1:
    screen = c.group.info()["screen"] # get the current active screen from qtile (zero base index)
    screen += 1 # turn the qtile screenindex from a zero base to a one base index
else:
    screen = int(argv[1])

path = "/home/berend/Pictures/screenshot_" + str(time.strftime("%Y-%m-%d %H-%M-%S")) + ".png"
#path.touch(exist_ok=True)

with mss() as sct:
    filname = sct.shot(mon=screen, output=path) # take screenshot and save it