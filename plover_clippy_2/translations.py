from plover.formatting import RetroFormatter
from .algos import tails


class Translations:
    def __init__(self, clippy):
        self.clippy = clippy
        self.english = None

    def getEnglish(self, phrase):
        return ''.join(RetroFormatter(phrase).last_fragments(999))

    def getStroked(self, phrase):
        return [y for x in phrase for y in x.rtfcre]

    def getSuggestions(self, english, stroked):
        lis = []
        for x in self.clippy.engine.get_suggestions(english):
            for y in x.steno_list:
                if len(y) < len(stroked):
                    lis.append(y)
        return lis

    def generator(self):
        self.english = None
        for phrase in tails(
                self.clippy.engine.translator_state.translations[-10:]):
            english = self.getEnglish(phrase)
            if english == self.english:
                continue
            self.english = english
            stroked = self.getStroked(phrase)
            suggestions = self.getSuggestions(english, stroked)
            if suggestions:
                yield english, stroked, suggestions
