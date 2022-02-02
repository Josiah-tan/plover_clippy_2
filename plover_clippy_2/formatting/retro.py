from datetime import datetime


class Retro:
    def getSuggestions(self, suggestions):
        return ", ".join("/".join(x) for x in suggestions)

    def getStroked(self, stroked):
        return "/".join(stroked)

    def format(self, phrase):
        suggestions = self.getSuggestions(
                phrase["suggestions"])
        stroked = self.getStroked(phrase["stroked"])
        return suggestions, stroked

    def suggest(self, obj, clippy):
        suggestions, stroked = self.format(clippy.state.phrase)
        english = clippy.state.phrase["english"]
        res = f'[{datetime.now().strftime("%F %T")}] {english:15} || ' \
              f'{stroked} -> ' \
              f'{suggestions}'
        clippy.actions.add(res)
