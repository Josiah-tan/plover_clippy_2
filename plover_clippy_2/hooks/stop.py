from ..util import getOrgDate
# from ..config import config
from ..default import Defaults


class Org:
    def defaultPre(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- STOP <{date}>")

    def defaultPost(self, clippy):
        pass


class Stop:
    def __init__(self, config):
        self.org = Org()
        self.config = config

    def pre(self, clippy):
        if hasattr(self.config, "stopPre"):
            self.config.stopPre(self, clippy)
        else:
            Defaults.stopPre(self, clippy)

    def post(self, clippy):
        if hasattr(self.config, "stopPost"):
            self.config.stopPost(self, clippy)
        else:
            Defaults.stopPost(self, clippy)
