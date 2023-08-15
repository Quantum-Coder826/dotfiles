from libqtile.command.client import InteractiveCommandClient

def SetTrayMax():

    c = InteractiveCommandClient()
    print(c.group["tray"].layout.maximize())

SetTrayMax()