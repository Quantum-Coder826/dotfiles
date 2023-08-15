#!/usr/bin/env python3
#!/usr/bin/env python3
import logging, sys
from libqtile.command.client import InteractiveCommandClient
from time import sleep

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG) # set the logging level.

c = InteractiveCommandClient()

def 