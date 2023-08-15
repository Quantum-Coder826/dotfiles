#!/usr/bin/env python3

import subprocess, sys

for line in subprocess.check_output(['wmctrl', '-l']).splitlines():
    window_name = line.split(None, 3)[-1].decode()
    print(window_name)
    if "A PipeWire Graph Qt GUI Interface" in window_name:
        print("Closing: qpwgraph")
        subprocess.call(['wmctrl', '-c', 'A PipeWire Graph Qt GUI Interface'])
        sys.exit() # exit program

# qpwgraph is not open so open it
    