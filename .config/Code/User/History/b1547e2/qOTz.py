#!/bin/env python3
from pypresence import Presence
import time

# get Client ID from file to protect it.
secret = open("secret.txt", "r")
client_id = secret.read()

RPC = Presence(client_id) # init client
RPC.connect()

RPC.update(state="Rich Presence using pypresence!")

while True:
    time.sleep(15)