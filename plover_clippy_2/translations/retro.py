from plover.formatting import RetroFormatter
from ..algos import tails


class Retro:
    def __init__(self):
        self.blocking = False

    def getEnglish(self, phrase):
        # tapey-tape hack with 0 meaning get all fragments
        return ''.join(RetroFormatter(phrase).last_fragments(0))

    def getStroked(self, phrase):
        return [y for x in phrase for y in x.rtfcre]

    def getSuggestions(self, clippy, english, stroked):
        lis = []
        for x in clippy.engine.get_suggestions(english):
            for y in x.steno_list:
                if len(y) < len(stroked):
                    lis.append(y)
        return lis

    def _generator(self, obj, clippy, translation_stack):
        last = None
        # for phrase in tails(
        #         clippy.engine.translator_state.translations[-10:]):
        for phrase in tails(translation_stack):
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

    def generator(self, obj, clippy):
        last_num_translations = clippy.state.last_num_translations
        translations = clippy.engine.translator_state.translations
        yield from self._generator(
                obj, clippy,
                translations[-last_num_translations:])

    def filter(self, obj, clippy):
        for a in reversed(obj.new):
            if a.text and not a.text.isspace():
                return True
        return False
