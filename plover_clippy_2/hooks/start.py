from ..util import getOrgDate
from ..config import Config
from ..default import Defaults


class Start:
    def __init__(self):
        pass

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

    def orgDefaultPre(self, clippy):
        date = getOrgDate()
        return clippy.actions.add(f"- START <{date}>")

    def orgDefaultPost(self, clippy):
        pass
