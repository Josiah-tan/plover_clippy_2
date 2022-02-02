from .retro import Retro
from .org import Org


class Formatting:
    def __init__(self):
        self.retro = Retro()
        self.org = Org()

    def minimalSuggest(self, obj, clippy):
        phrase = clippy.state.phrase
        suggestions = self.retro.getSuggestions(phrase["suggestions"])
        max_pad_english = clippy.state.max_pad_english
        english = phrase["english"]
        return clippy.actions.add(
                f'{english:{max_pad_english}} '
                f'{suggestions}'
                )
