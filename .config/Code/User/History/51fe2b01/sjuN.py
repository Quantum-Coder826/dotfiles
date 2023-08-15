#!/usr/bin/env python3

import subprocess

for line in subprocess.check_output(['wmctrl', '-l']).splitlines():
    window_name = line.split(None, 3)[-1].decode()
    if "A PipeWire Graph Qt GUI Interface" in window_name:
        print("")
        subprocess.call(['wmctrl', '-c', '"A PipeWire Graph Qt GUI Interface"'])
    else:
        print("Opening: qpwgrath")
