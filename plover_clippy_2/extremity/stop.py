from ..util import getOrgDate
from plover_clippy_2.formatting.color import Color


class Stop(Color):
    def __init__(self, colorscheme=None, mode=None, colors=None):
        super().__init__(colorscheme, colors)
        if mode is None:
            self.mode = self.defaultPre
        else:
            self.mode = getattr(self, mode)
        self.output = None

    def preprocess(self, obj, clippy):
        self.STOP = "STOP"
        self.date = getOrgDate()

    def stop(self, obj, clippy):
        self.mode(obj, clippy)

    def defaultPre(self, obj, clippy):
        self.output = f"- {self.STOP} {self.date}"
