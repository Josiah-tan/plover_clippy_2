from ..util import getOrgDate
# from ..config import config
from ..default import Defaults


class Org:
    def defaultPre(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- START <{date}>")

    def defaultPost(self, clippy):
        pass


class Start:
    def __init__(self, config):
        self.org = Org()
        self.config = config

    def pre(self, clippy):
        if hasattr(self.config, "startPre"):
            self.config.startPre(self, clippy)
        else:
            Defaults.startPre(self, clippy)

    def post(self, clippy):
        if hasattr(self.config, "startPost"):
            self.config.startPost(self, clippy)
        else:
            Defaults.startPost(self, clippy)
