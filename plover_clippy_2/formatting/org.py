from .retro import Retro


class Org:
    def __init__(self):
        self.retro = Retro()

    def getEfficiencySymbol(
            self, clippy, efficiency_symbol,
            stroked, suggestions):
        num = len(stroked) - min(
                [len(x) for x in suggestions])
        assert num > 0
        return efficiency_symbol * min(num, clippy.state.max_pad_efficiency)
        # return efficiency_symbol

    def format(self, obj, clippy):
        suggestions, stroked = self.retro.format(clippy.state.phrase)
        english = clippy.state.phrase["english"]
        efficiency_symbol = self.getEfficiencySymbol(
                clippy, clippy.state.efficiency_symbol,
                clippy.state.phrase["stroked"],
                clippy.state.phrase["suggestions"])
        max_pad_efficiency = clippy.state.max_pad_efficiency
        max_pad_english = clippy.state.max_pad_english
        return (
                suggestions, stroked, english,
                efficiency_symbol, max_pad_efficiency,
                max_pad_english)

    def defaultSuggest(self, obj, clippy):
        (
                suggestions, stroked, english,
                efficiency_symbol, max_pad_efficiency,
                max_pad_english
                ) = self.format(obj, clippy)
        return clippy.actions.add(
                f'{efficiency_symbol:{max_pad_efficiency}}'
                f' {english:{max_pad_english}} '
                f'{suggestions} < {stroked}')

    def debugSuggest(self, obj, clippy):
        (
                suggestions, stroked, english,
                efficiency_symbol, max_pad_efficiency,
                max_pad_english
                ) = self.format(obj, clippy)
        return clippy.actions.add(
                f'{efficiency_symbol:{max_pad_efficiency}}'
                f' {english:{max_pad_english}} '
                f'{suggestions} < {stroked}  '
                f'# {clippy.state.phrase["source"]}')

    def minimalSuggest(self, obj, clippy):
        (
                suggestions, stroked, english,
                efficiency_symbol, max_pad_efficiency,
                max_pad_english
                ) = self.format(obj, clippy)
        return clippy.actions.add(
                f'{efficiency_symbol:{max_pad_efficiency}}'
                f' {english:{max_pad_english}} '
                f'{suggestions}'
                )
