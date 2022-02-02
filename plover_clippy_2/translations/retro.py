from plover.formatting import RetroFormatter
from ..algos import tails


class Retro:
    def getEnglish(self, phrase):
        return ''.join(RetroFormatter(phrase).last_fragments(999))

    def getStroked(self, phrase):
        return [y for x in phrase for y in x.rtfcre]

    def getSuggestions(self, clippy, english, stroked):
        lis = []
        for x in clippy.engine.get_suggestions(english):
            for y in x.steno_list:
                if len(y) < len(stroked):
                    lis.append(y)
        return lis

    def generator(self, obj, clippy):
        last = None
        for phrase in tails(
                clippy.engine.translator_state.translations[-10:]):
            english = self.getEnglish(phrase)
            if english == last:
                continue
            last = english
            stroked = self.getStroked(phrase)
            suggestions = self.getSuggestions(clippy, english, stroked)
            if suggestions:
                yield {"english": english,
                       "stroked": stroked,
                       "suggestions": suggestions}

    def filter(self, obj, clippy):
        for a in reversed(obj.new):
            if a.text and not a.text.isspace():
                return True
        return False
