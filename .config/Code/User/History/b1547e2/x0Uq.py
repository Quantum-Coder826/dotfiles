#!/bin/env python3
from pypresence import presence
import time

client_id = "1114079479954952202"
RPC = presence(client_id)

RPC.connect()

RPC.update(state="Rich Presence using pypresence!")

while True:
    time.sleep(15)