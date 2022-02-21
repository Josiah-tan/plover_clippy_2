from ..util import getOrgDate
from ..config import config
from ..default import Defaults


class Org:
    def defaultPost(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- INIT <{date}>")

    def defaultPre(self, clippy):
        pass


class Initialize:
    def __init__(self):
        self.org = Org()

    def pre(self, clippy):
        if hasattr(config, "initPre"):
            config.initPre(self, clippy)
        else:
            Defaults.initPre(self, clippy)

    def post(self, clippy):
        if hasattr(config, "initPost"):
            config.initPost(self, clippy)
        else:
            Defaults.initPost(self, clippy)
