from libqtile.command.client import InteractiveCommandClient
from libqtile.config import hook

c = InteractiveCommandClient()

@hook.subscribe.group_window_add