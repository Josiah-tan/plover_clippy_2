from .retro import Retro


class Tkfps:
    """
    suggestion source for TK-FPS (retrospective delete space)
    """

    def __init__(self, stroke=("TK-FPS",)):
        self.len_translation_stack = 0
        self.blocking = False
        self.stroke = stroke
        self.retro = Retro()

    def filter(self, obj, clippy):
        """
        when TK-FPS pressed,
        top of translation stack goes from ["type", "writer"]
        -> ["type{^~|^}writer"]
        """
        translation_stack = clippy.engine.translator_state.translations
        len_translation_stack = len(translation_stack)
        res = (
                self.len_translation_stack > 1 and
                translation_stack[-1].rtfcre == self.stroke and
                self.len_translation_stack == len_translation_stack + 1)
        if not res and len_translation_stack >= 2:
            self.cache = translation_stack[-2:]
        self.len_translation_stack = len_translation_stack
        return res

    def getStroked(self, phrase):
        """
        same thing as retro.getStroked,
        just convert ["TK-FPS"]
        -> ["type", "writer", "TK-FPS"]
        """
        lis = []
        for x in phrase:
            if x.rtfcre == self.stroke:
                lis += self.retro.getStroked(self.cache)
            for y in x.rtfcre:
                lis += [y]
        return lis
        # return [y for x in phrase for y in x.rtfcre]

    def generator(self, obj, clippy):
        translation_stack = clippy.engine.translator_state.translations
        phrase = translation_stack[-1:]  # list
        english = self.retro.getEnglish(phrase)
        stroked = self.getStroked(phrase)
        suggestions = self.retro.getSuggestions(clippy, english, stroked)
        if suggestions:
            yield {"english": english,
                   "stroked": stroked,
                   "suggestions": suggestions}
