#!/usr/bin/env python3

from pynput.mouse import Button, Controller
import sys

mouse = Controller()

saved_mouse_pos = mouse.position # save the mouse postion

mouse.position = (1709, 1060)
mouse.click(Button.left)

mouse.position = saved_mouse_pos

sys.exit()