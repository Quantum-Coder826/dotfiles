#!/usr/bin/env python3

from libqtile.command.client import InteractiveCommandClient
from mss.linux import MSS as mss
from datetime import datetime
import sys

#c = InteractiveCommandClient()

time = datetime.now()

# this variable is used to set wich screen is captured
# -1 for all screens
# 1 for main monitor
# 2 for secondairy

if len(sys.argv) == 0:
    screen = -1
else:
    screen = sys.argv[0]
screen = 1

path = "/home/berend/Pictures/screenshot_" + str(time.strftime("%Y-%m-%d %H-%M-%S")) + ".png"
#path.touch(exist_ok=True)

with mss() as sct:
    filname = sct.shot(mon=screen, output=path)