from .repeat import Repeat
from ..sources import Sources


class Distillations:
    def __init__(self):
        self.sources = Sources([Repeat])

    def distill(self, obj, clippy):
        for source in self.sources.get():
            if not source.distill(obj, clippy):
                return False
        return True
