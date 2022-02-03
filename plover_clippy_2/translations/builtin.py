from ..algos import tails
from .org import Org
from .retro import Retro
from .finger_spelling import FingerSpelling


class Translations:
    def __init__(self):
        self.org = Org()
        self.retro = Retro()
        self.finger = FingerSpelling()

    def _generator(self, obj, clippy, translation_stack):
        last = None
        for phrase in tails(translation_stack):
            english = self.retro.getEnglish(phrase)
            if english == last:
                continue
            last = english
            stroked = self.retro.getStroked(phrase)
            suggestions = self.retro.getSuggestions(clippy, english, stroked)
            if suggestions:
                yield {"english": english,
                       "stroked": stroked,
                       "suggestions": suggestions}

    def generator(self, obj, clippy):
        translation_stack = clippy.engine.translator_state.translations
        last_num_translations = clippy.state.last_num_translations
        yield from self.finger.generator(obj, clippy)
        yield from self._generator(
                obj, clippy, translation_stack[-last_num_translations:])

    def filter(self, obj, clippy):
        fingerSpelling = self.finger.filter(obj, clippy)
        retro = self.retro.filter(obj, clippy)
        return fingerSpelling and retro
