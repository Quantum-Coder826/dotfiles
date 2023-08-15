from libqtile.command.client import InteractiveCommandClient
from libqtile.config import hook

c = InteractiveCommandClient()

c.group["tray"].layout.maximize # maximize the manepane of the monadtall layout in the tray group
