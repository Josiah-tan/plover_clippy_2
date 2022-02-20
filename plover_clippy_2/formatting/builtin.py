from ..sources import Sources
# from .gruvbox import Gruvbox
from .retro import Retro
from .org import Org


class Formatting:
    def __init__(self):
        # self.retro = Retro()
        # self.org = Org()
        # self.gruvbox = Gruvbox()
        self.sources = Sources([Org, Retro])

    def suggest(self, obj, clippy):
        self.sources.wrapColor(obj, clippy, "format")
