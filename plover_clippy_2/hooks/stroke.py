# from util import getOrgDate
from ..config import Config
from ..default import Defaults


class Org:
    def defaultPre(self, obj, clippy):
        clippy.state.prev_stroke = obj.stroke

    def defaultPost(self, obj, clippy):
        pass


class OnStroked:
    def __init__(self, stroke):
        self.org = Org()
        self.stroke = stroke

    def pre(self, clippy):
        if hasattr(Config, "onStrokedPre"):
            Config.onStrokedPre(self, clippy)
        else:
            Defaults.onStrokedPre(self, clippy)

    def post(self, clippy):
        if hasattr(Config, "onStrokedPost"):
            Config.onStrokedPost(self, clippy)
        else:
            Defaults.onStrokedPost(self, clippy)
