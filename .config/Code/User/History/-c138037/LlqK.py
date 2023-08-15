from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()
print(c.group["tray"].a())
