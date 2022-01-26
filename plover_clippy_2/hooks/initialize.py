from ..util import getOrgDate
from ..config import Config
from ..default import Defaults


class Initialize:
    def __init__(self):
        pass

    def pre(self, clippy):
        if hasattr(Config, "initPre"):
            Config.initPre(self, clippy)
        else:
            Defaults.initPre(self, clippy)

    def post(self, clippy):
        if hasattr(Config, "initPost"):
            Config.initPost(self, clippy)
        else:
            Defaults.initPost(self, clippy)

    def orgDefaultPost(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- INIT <{date}>")

    def orgDefaultPre(self, clippy):
        pass
