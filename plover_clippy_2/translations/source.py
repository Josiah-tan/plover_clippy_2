from .retro import Retro
from .finger_spelling import FingerSpelling
from .undo import Undo
from .tk_fps import TKFPS


class Sources:
    def __init__(self, val=None):
        self._cls_available = [Undo, FingerSpelling, Retro, TKFPS]
        self._str_available = self.str(self._cls_available)
        self._sources = None

    def str(self, sources):
        res = []
        for source in sources:
            res.append(source.__name__)
        return res

    def get(self):
        return self._sources

    def set(self, *val):
        self._sources = ()
        for source in val:
            if type(source) == str:
                source = self._cls_available[self._str_available.index(source)]
            self._sources += (source(),)

    def append(self, *val):
        sources = self.get()
        self.set(*val)
        self._sources = sources + self.get()

    def prepend(self, *val):
        sources = self.get()
        self.set(*val)
        self._sources = self.get() + sources

# i = Sources()
# i.set("Retro")
# i.get()
# i.append("Org")
# i.prepend("Undo", "FingerSpelling")
# i.get()
# i.append("TKFPS")
# i.get()
