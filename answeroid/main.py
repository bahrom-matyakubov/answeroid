import threading
from answeroid.droid import Answeroid
from helpers.gcal import Gcal
from helpers.wolf import Wolf
from helpers.bing import Bing
from sites.common import Site


class BotThread(threading.Thread):
    def __init__(self, site, helper):
        threading.Thread.__init__(self)
        self.droid = Answeroid(site, helper)
        self.run = self.droid.watch


with Site() as ste:
    gcal = BotThread(ste, Gcal())
    wolf = BotThread(ste, Wolf())
    bing = BotThread(ste, Bing())
    gcal.start()
    wolf.start()
    bing.start()
    gcal.join()
    wolf.join()
    bing.join()
