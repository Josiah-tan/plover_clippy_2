from ..util import getOrgDate
# from ..config import config
from ..default import Defaults


class Org:
    def defaultPost(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- INIT <{date}>")

    def defaultPre(self, clippy):
        pass


class Initialize:
    def __init__(self, config):
        self.config = config
        self.org = Org()

    def pre(self, clippy):
        if hasattr(self.config, "initPre"):
            self.config.initPre(self, clippy)
        else:
            Defaults.initPre(self, clippy)

    def post(self, clippy):
        if hasattr(self.config, "initPost"):
            self.config.initPost(self, clippy)
        else:
            Defaults.initPost(self, clippy)
