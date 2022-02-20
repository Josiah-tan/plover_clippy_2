from ..util import getOrgDate
from plover_clippy_2.formatting.color import Color


class Start(Color):
    def __init__(self, colorscheme=None, mode=None, colors=None):
        super().__init__(colorscheme, colors)
        if mode is None:
            self.mode = self.defaultPre
        else:
            self.mode = getattr(self, mode)
        self.output = None

    def preprocess(self, obj, clippy):
        self.START = "START"
        self.date = getOrgDate()

    def start(self, obj, clippy):
        self.mode(obj, clippy)

    def defaultPre(self, obj, clippy):
        self.output = f"- {self.START} {self.date}"
