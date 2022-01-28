# from util import getOrgDate
from datetime import datetime
from ..config import Config
from ..default import Defaults


class OnTranslate:
    def __init__(self):
        pass

    def pre(self, clippy):
        if hasattr(Config, "onTranslatePre"):
            Config.onTranslatePre(self, clippy)
        else:
            Defaults.onTranslatePre(self, clippy)

    def call(self, clippy):
        if hasattr(Config, "onTranslateCall"):
            Config.onTranslateCall(self, clippy)
        else:
            Defaults.onTranslateCall(self, clippy)

    def post(self, clippy):
        if hasattr(Config, "onTranslatePost"):
            Config.onTranslatePost(self, clippy)
        else:
            Defaults.onTranslatePost(self, clippy)

    def orgDefaultPre(self, clippy):
        pass

    def orgDefaultPost(self, clippy):
        pass

    def formatSuggestions(self, suggestions):
        return ", ".join("/".join(x) for x in suggestions)

    def formatStroked(self, stroked):
        return "/".join(stroked)

    def formatEfficiencySymbol(self, clippy, efficiency_symbol):
        num = len(clippy.state.stroked) - min(
                [len(x) for x in clippy.state.suggestions])
        assert num > 0
        return efficiency_symbol * min(num, clippy.state.max_pad_efficiency)

    def orgDefaultCall(self, clippy):
        # *     {#escape}       TPEFBG < SKWHEUFPL/SKWH-FRLG/SKA*EUP/SKWHEURBG
        # obj.orgDefaultPost(clippy)
        # return clippy.add(f"{"*":{clippy.max_pad_efficiency}}{obj.english:max_pad_english} {obj.stroked} < {obj.suggestions}")
        # obj.default_post(clippy)
        suggestions = self.formatSuggestions(clippy.state.suggestions)
        english = clippy.state.english
        stroked = self.formatStroked(clippy.state.stroked)
        efficiency_symbol = self.formatEfficiencySymbol(
                clippy, clippy.state.efficiency_symbol)
        max_pad_efficiency = clippy.state.max_pad_efficiency
        max_pad_english = clippy.state.max_pad_english
        return clippy.actions.add(
                f'{efficiency_symbol:{max_pad_efficiency}}'
                f' {english:{max_pad_english}} '
                f'{suggestions} < {stroked}')

    def clippyDefaultCall(self, clippy):
        suggestions = self.formatSuggestions(clippy.state.suggestions)
        english = clippy.state.english
        stroked = self.formatStroked(clippy.state.stroked)
        res = f'[{datetime.now().strftime("%F %T")}] {english:15} || ' \
              f'{stroked} -> ' \
              f'{suggestions}'
        clippy.actions.add(res)
