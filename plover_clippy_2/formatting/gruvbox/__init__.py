from ..org import Org
from .pallete import pallete


class Gruvbox:
    def __init__(self):
        self.org = Org()
        self.str2val = dict()

    @staticmethod
    def _rgb(rgb):
        if type(rgb) == str:
            rgb = int(rgb, 16)
        return ((rgb >> 16) & 0xff, (rgb >> 8) & 0xff, rgb & 0xff)

    def preprocess(self, colors):
        """processes colors dictionary inplace"""
        for key, value in colors.items():
            _value = self.str2val.get(key)
            if callable(value):
                if _value is None:
                    raise NotImplementedError
                colors[key] = value(_value)
                value = colors[key]
            if value in pallete:  # in color pallete
                value = colors[key] = pallete[value]
            if type(value) == int:  # ansi
                colors[key] = f"\033[38;5;{value}m"
            elif (value[0] == "#" and
                    len(value) == 7 and
                    value[1:].isnumeric):  # hex
                red, green, blue = self._rgb(value[1:])
                colors[key] = f"\033[38;2;{red};{green};{blue}m"
            elif value[0] == "\033":  # ansi color code
                continue
            else:
                raise ValueError(f"invalid input: {value}")

    def preAdd(colors):
        pass
        # problem, if we only color one character and then terminate it 
        # the rest of the string would be no coloured
        # for key, value in colors.items():
        #     _value = self.str2val.get(key)
        #     if _value:
        #         continue
        #     for k, v in self.str2val.items():
        #         self.addColor()

    def add(self, colors):
        for key, value in colors.items():
            _value = self.str2val.get(key)
            if _value:
                self.str2val[key] = value+self.str2val[key]+"\u001b[0m"

    def format(self, obj, clippy):
        colors = clippy.state.gruvbox_colors
        (
                suggestions, stroked, english,
                efficiency_symbol, max_pad_efficiency,
                max_pad_english
                ) = self.org._format(obj, clippy)
        self.str2val["suggestions"] = suggestions
        self.str2val["stroked"] = stroked
        self.str2val["english"] = english
        self.str2val["efficiency_symbol"] = efficiency_symbol
        self.str2val["source"] = f"# {clippy.state.phrase['source']}"

        self.preprocess(colors)
        # self.preAdd(colors)
        self.add(colors)

        return (
                self.str2val["suggestions"], self.str2val["stroked"],
                self.str2val["english"], self.str2val["efficiency_symbol"],
                max_pad_efficiency, max_pad_english, self.str2val["source"])

    def debugSuggest(self, obj, clippy):
        (
                suggestions, stroked, english,
                efficiency_symbol, max_pad_efficiency,
                max_pad_english, source
                ) = self.format(obj, clippy)
        return clippy.actions.add(
                f'{efficiency_symbol:{max_pad_efficiency}}'
                f' {english:{max_pad_english}} '
                f'{suggestions} < {stroked}  '
                f'{source}')
