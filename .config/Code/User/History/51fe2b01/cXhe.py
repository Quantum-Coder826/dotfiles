#!/usr/bin/env python3

from pynput.mouse import Button, Controller
import sys

mouse = Controller()

saved_mouse_pos = mouse.position # save the mouse postion

mouse.position = (1709, 1060) # move the mouse to the qpwgraph tray icon and click
mouse.press(Button.left)
mouse.release(Button.left)

mouse.position = saved_mouse_pos # restore the mouse postion

sys.exit()