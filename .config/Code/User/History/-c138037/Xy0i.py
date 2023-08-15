from libqtile.command.client import InteractiveCommandClient
from steam.client import

c = InteractiveCommandClient()
print(c.group["tray"].window.info())