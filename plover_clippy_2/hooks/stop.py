from ..util import getOrgDate
from ..config import config
from ..default import Defaults


class Org:
    def defaultPre(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- STOP <{date}>")

    def defaultPost(self, clippy):
        pass


class Stop:
    def __init__(self):
        self.org = Org()

    def pre(self, clippy):
        if hasattr(config, "stopPre"):
            config.stopPre(self, clippy)
        else:
            Defaults.stopPre(self, clippy)

    def post(self, clippy):
        if hasattr(config, "stopPost"):
            config.stopPost(self, clippy)
        else:
            Defaults.stopPost(self, clippy)
