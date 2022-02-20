from .palletes import gruvbox
from plover_clippy_2.algos.color import getStandardAnsi, wrapAnsi


class Color:
    def __init__(self, colorscheme=None, colors=None):
        self.colorscheme = colorscheme
        self.colors = colors

        self.pallete = self.getPallete(self.colorscheme)

    def getPallete(self, colorscheme="gruvbox"):
        if colorscheme == "gruvbox":
            return gruvbox

    def getAnsi(self, key, value):
        if callable(value):
            value = value(getattr(self, key))
        if self.pallete and value in self.pallete:
            value = self.pallete[value]
        return getStandardAnsi(value)

    def addColor(self, obj, clippy):
        if self.colors is None:
            self.colors = clippy.state.colors
            if not clippy.state.colors:
                return
        for key, val in self.colors.items():
            if hasattr(self, key):
                color = self.getAnsi(key, val)
                setattr(self, key, wrapAnsi(color, getattr(self, key)))

    def extraColor(self, obj, clippy):
        pass
