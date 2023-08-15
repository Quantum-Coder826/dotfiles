#!/usr/bin/env python3

from libqtile.command.client import InteractiveCommandClient
from mss.linux import MSS as mss
from datetime import datetime
from sys import argv

#c = InteractiveCommandClient()

time = datetime.now()

# this variable is used to set wich screen is captured
# -1 for all screens
# 1 for main monitor
# 2 for secondairy
print(argv)

if len(argv) > 1:
    screen = -1
else:
    screen = argv[0]
screen = 1

path = "/home/berend/Pictures/screenshot_" + str(time.strftime("%Y-%m-%d %H-%M-%S")) + ".png"
#path.touch(exist_ok=True)

with mss() as sct:
    filname = sct.shot(mon=screen, output=path)