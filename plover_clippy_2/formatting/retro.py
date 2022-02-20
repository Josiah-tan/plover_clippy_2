from .color import Color
from datetime import datetime


class Retro(Color):
    def __init__(self, colorscheme=None, mode=None, colors=None):
        super().__init__(colorscheme, colors)
        if mode is None:
            self.mode = self.defaultSuggest
        else:
            self.mode = getattr(self, mode)
        self.output = None

    def getSuggestions(self, suggestions):
        return ", ".join("/".join(x) for x in suggestions)

    def getStroked(self, stroked):
        return "/".join(stroked)

    def getEnglish(self, clippy, english):
        pad = clippy.state.max_pad_english
        return clippy.state.justify(english, pad)

    def preprocess(self, obj, clippy):
        phrase = clippy.state.phrase
        self.suggestions = self.getSuggestions(
                phrase["suggestions"])
        self.stroked = self.getStroked(phrase["stroked"])
        self.english = self.getEnglish(
                clippy, clippy.state.phrase["english"])

    def format(self, obj, clippy):
        self.mode(obj, clippy)

    def defaultSuggest(self, obj, clippy):
        suggestions = self.suggestions
        stroked = self.stroked
        english = self.english
        self.output = (
                f'[{datetime.now().strftime("%F %T")}] {english} || '
                f'{stroked} -> '
                f'{suggestions}'
                )

    def minimalSuggest(self, obj, clippy):
        suggestions = self.suggestions
        english = self.english
        return clippy.actions.add(
                f'{english} '
                f'{suggestions}'
                )
