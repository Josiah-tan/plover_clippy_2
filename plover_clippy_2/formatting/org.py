from .retro import Retro
from .color import Color


class Org(Color):
    def __init__(self, colorscheme=None, mode=None, colors=None):
        super().__init__(colorscheme, colors)
        self.retro = Retro()
        if mode is None:
            self.mode = self.defaultSuggest
        else:
            self.mode = getattr(self, mode)
        self.output = None

    def getEfficiencySymbol(
            self, clippy, stroked, suggestions):
        num = len(stroked) - min(
                [len(x) for x in suggestions])
        assert num > 0
        efficiency_symbol = clippy.state.efficiency_symbol
        max_pad_efficiency = clippy.state.max_pad_efficiency
        res = efficiency_symbol * min(num, max_pad_efficiency)
        return clippy.state.justify(res, max_pad_efficiency)
        # return efficiency_symbol

    def preprocess(self, obj, clippy):
        phrase = clippy.state.phrase
        self.suggestions = self.retro.getSuggestions(
                phrase["suggestions"])
        self.stroked = self.retro.getStroked(
                phrase["stroked"])
        self.english = self.retro.getEnglish(
                clippy, clippy.state.phrase["english"])
        self.efficiency_symbol = self.getEfficiencySymbol(
                clippy, phrase["stroked"], phrase["suggestions"])
        self.source = f'# {phrase["source"]}'

    def format(self, obj, clippy):
        self.mode(obj, clippy)

    def defaultSuggest(self, obj, clippy):
        stroked = self.stroked
        suggestions = self.suggestions
        english = self.english
        efficiency_symbol = self.efficiency_symbol
        # self.output = (
        #         f'{efficiency_symbol:{max_pad_efficiency}}'
        #         f' {english:{max_pad_english}} '
        #         f'{suggestions} < {stroked}')
        self.output = (
                f'{efficiency_symbol}'
                f' {english} '
                f'{suggestions} < {stroked}')

    def debugSuggest(self, obj, clippy):
        stroked = self.stroked
        suggestions = self.suggestions
        english = self.english
        efficiency_symbol = self.efficiency_symbol
        source = self.source
        self.output = (
                f'{efficiency_symbol}'
                f' {english} '
                f'{suggestions} < {stroked}  '
                f'{source}')

    def minimalSuggest(self, obj, clippy):
        suggestions = self.suggestions
        english = self.english
        efficiency_symbol = self.efficiency_symbol
        self.output = (
                f'{efficiency_symbol}'
                f' {english} '
                f'{suggestions}'
                )
