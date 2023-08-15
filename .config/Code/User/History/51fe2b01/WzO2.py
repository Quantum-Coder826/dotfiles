#!/usr/bin/env python3

import subprocess

for line in subprocess.check_output(['wmctrl', '-l']).splitlines():
    window_name = line.split(None, 3)[-1].decode()
    if window_name
