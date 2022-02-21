from ..util import getOrgDate
from ..config import config
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
        if hasattr(config, "startPre"):
            config.startPre(self, clippy)
        else:
            Defaults.startPre(self, clippy)

    def post(self, clippy):
        if hasattr(config, "startPost"):
            config.startPost(self, clippy)
        else:
            Defaults.startPost(self, clippy)
