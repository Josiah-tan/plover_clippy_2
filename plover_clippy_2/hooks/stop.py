from ..util import getOrgDate
from ..config import Config
from ..default import Defaults


class Stop:
    def __init__(self):
        pass

    def pre(self, clippy):
        if hasattr(Config, "stopPre"):
            Config.stopPre(self, clippy)
        else:
            Defaults.stopPre(self, clippy)

    def post(self, clippy):
        if hasattr(Config, "stopPost"):
            Config.stopPost(self, clippy)
        else:
            Defaults.stopPost(self, clippy)

    def orgDefaultPre(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- STOP <{date}>")

    def orgDefaultPost(self, clippy):
        pass
