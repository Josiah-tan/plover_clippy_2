# from ..algos import tails
from .org import Org
from .source import Sources


class Translations:
    def __init__(self):
        self.org = Org()

        # available suggestion sources
        # self.retro = Retro()
        # self.finger = FingerSpelling()
        # self.undo = Undo()
        # self.tkfps = TKFPS()

        self.sources = Sources()
        # self.sources = [self.undo, self.finger, self.retro, TKFPS()]
        # self.sources.set(Undo, FingerSpelling, Retro, TKFPS)
        self._filter = None

    def generator(self, obj, clippy):
        # translation_stack = clippy.engine.translator_state.translations
        # last_num_translations = clippy.state.last_num_translations

        # yield from self.finger.generator(obj, clippy)
        # yield from self.retro.generator(obj, clippy)

        # yield from self._generator(
        #         obj, clippy, translation_stack[-last_num_translations:])

        for idx, source in enumerate(self.sources.get()):
            if hasattr(source, "generator") and self._filter[idx]:
                for gen in source.generator(obj, clippy):
                    gen["source"] = source.__class__.__name__
                    yield gen
                # yield from source.generator(obj, clippy)

    def filter(self, obj, clippy):
        # undo = self.undo.filter(obj, clippy)
        # fingerSpelling = self.finger.filter(obj, clippy)
        # retro = self.retro.filter(obj, clippy)
        # return undo and fingerSpelling and retro

        res = False
        self._filter = [False] * len(self.sources.get())
        for idx, source in enumerate(self.sources.get()):
            if hasattr(source, "filter"):
                if source.filter(obj, clippy):
                    res = True
                    self._filter[idx] = True
                elif source.blocking:
                    return False
        return res

