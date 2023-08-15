from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()
print(c.group["tray"].window.info())

def setFormat():
    while range(0,5):
        c.group["tray"]