from libqtile.command.client import InteractiveCommandClient
from time import sleep

c = InteractiveCommandClient()

sleep(1)
c.group["tray"].layout.maximize() # maximize the manepane of the monadtall layout in the tray group
