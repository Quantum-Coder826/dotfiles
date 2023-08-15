#!/usr/bin/env python3

from pynput.mouse import Button, Controller
from time import sleep
import sys

mouse = Controller()

saved_mouse_pos = mouse.position # save the mouse postion

mouse.position = (1709, 1060) # move the mouse to the qpwgraph tray icon and click
sleep(100/1000)
mouse.click(Button.left)

mouse.position = saved_mouse_pos # restore the mouse postion

sys.exit()