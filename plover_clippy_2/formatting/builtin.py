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
        print("Hello world")
        for source in self.sources.get():
            if hasattr(source, "preprocess"):
                source.preprocess(obj, clippy)
            if hasattr(source, "addColor"):
                source.addColor(obj, clippy)
            if hasattr(source, "format"):
                source.format(obj, clippy)
            if hasattr(source, "extraColor"):
                source.extraColor(obj, clippy)
            if source.output:
                clippy.actions.add(source.output)
