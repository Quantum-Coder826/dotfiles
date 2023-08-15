#!/bin/env python3
from pypresence import Presence
import time

client_id = "1114079479954952202"
RPC = Presence(client_id)

RPC.connect()

RPC.update(state="Rich Presence using pypresence!")

while True:
    time.sleep(15)