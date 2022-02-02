from ..util import getOrgDate
from ..config import Config
from ..default import Defaults


class Org:
    def defaultPre(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- START <{date}>")

    def defaultPost(self, clippy):
        pass


class Start:
    def __init__(self):
        self.org = Org()

    def pre(self, clippy):
        if hasattr(Config, "startPre"):
            Config.startPre(self, clippy)
        else:
            Defaults.startPre(self, clippy)

    def post(self, clippy):
        if hasattr(Config, "startPost"):
            Config.startPost(self, clippy)
        else:
            Defaults.startPost(self, clippy)
