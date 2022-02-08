# from ..algos import tails
from .org import Org
from .retro import Retro
from .finger_spelling import FingerSpelling
from .undo import Undo
from .tk_fps import TKFPS


class Translations:
    def __init__(self):
        self.org = Org()
        # self.retro = Retro()
        # self.finger = FingerSpelling()
        # self.undo = Undo()
        # self.sources = [self.undo, self.finger, self.retro, TKFPS()]
        self.sources = [Undo(), FingerSpelling(), Retro(), TKFPS()]
        self._filter = None

    # def _generator(self, obj, clippy, translation_stack):
    #     last = None
    #     for phrase in tails(translation_stack):
    #         english = self.retro.getEnglish(phrase)
    #         if english == last:
    #             continue
    #         last = english
    #         stroked = self.retro.getStroked(phrase)
    #         suggestions = self.retro.getSuggestions(clippy, english, stroked)
    #         if suggestions:
    #             yield {"english": english,
    #                    "stroked": stroked,
    #                    "suggestions": suggestions}

    def generator(self, obj, clippy):
        # translation_stack = clippy.engine.translator_state.translations
        # last_num_translations = clippy.state.last_num_translations

        # yield from self.finger.generator(obj, clippy)
        # yield from self.retro.generator(obj, clippy)

        # yield from self._generator(
        #         obj, clippy, translation_stack[-last_num_translations:])

        for idx, source in enumerate(self.sources):
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
        self._filter = [False] * len(self.sources)
        for idx, source in enumerate(self.sources):
            if hasattr(source, "filter"):
                if source.filter(obj, clippy):
                    res = True
                    self._filter[idx] = True
                elif source.blocking:
                    return False
        return res
