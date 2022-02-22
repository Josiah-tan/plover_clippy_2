# from util import getOrgDate
# from ..config import config
from ..default import Defaults


class Org:
    def defaultPre(self, obj, clippy):
        clippy.state.prev_stroke = obj.stroke

    def defaultPost(self, obj, clippy):
        pass


class OnStroked:
    def __init__(self, config, stroke):
        self.org = Org()
        self.config = config
        self.stroke = stroke

    def pre(self, clippy):
        if hasattr(self.config, "onStrokedPre"):
            self.config.onStrokedPre(self, clippy)
        else:
            Defaults.onStrokedPre(self, clippy)

    def post(self, clippy):
        if hasattr(self.config, "onStrokedPost"):
            self.config.onStrokedPost(self, clippy)
        else:
            Defaults.onStrokedPost(self, clippy)
