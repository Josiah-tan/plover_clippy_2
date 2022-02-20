from plover_clippy_2.formatting.gruvbox import Gruvbox

from importlib import reload
import plover_clippy_2.formatting.gruvbox
reload(plover_clippy_2.formatting.gruvbox)

colors = {
        "suggestions": lambda suggestions: "#1d2021",
        "stroked": "\033[95m",
        "english": 5,
        # "english": 5,
        "efficiency_symbol": lambda efficiency_symbol: [
            "bright_green", "bright_purple", "bright_blue",
            "bright_orange", "bright_red"
            ][min(len(efficiency_symbol)-1, 4)],
        "*": "gray",
        ">": "gray",
        # "pad_efficiency": background support needed
        # "pad_english": background
        "source": "gray"
        }

assert callable(colors["suggestions"])
assert not callable(colors["stroked"])
assert not callable(colors["english"])

assert "\033[95m"[0] == "\033"
assert "\033[95m"[0] == "\u001b"

assert "1234".isnumeric()

assert Gruvbox()._rgb("0000A0") == (0, 0, 160)


gruvbox = Gruvbox()
gruvbox.str2val = {
    "suggestions": "HAEP, HAEFP, HAP/PEU, HAP/KWREU",
    "stroked": "H*/A*/P*/P*/KWR*",
    "english": "happy",
    "efficiency_symbol": "***",
    "source": "# FingerSpelling"
    }
gruvbox.preprocess(colors)
colors
assert colors == {'suggestions': '\x1b[38;2;29;32;33m', 'stroked': '\x1b[95m', 'english': '\x1b[38;5;5m', 'efficiency_symbol': '\x1b[38;2;254;128;25m', '*': '\x1b[38;2;146;131;116m', '>': '\x1b[38;2;146;131;116m'}
gruvbox.add(colors)
gruvbox.str2val

max_pad_english = 15
max_pad_efficiency = 5

suggestions, stroked, english, efficiency_symbol, max_pad_efficiency, max_pad_english, source = (gruvbox.str2val["suggestions"], gruvbox.str2val["stroked"], gruvbox.str2val["english"], gruvbox.str2val["efficiency_symbol"], max_pad_efficiency, max_pad_english, gruvbox.str2val["source"])
print(
        f'{efficiency_symbol:{max_pad_efficiency}}'
        f' {english:{max_pad_english}} '
        f'{suggestions} < {stroked}  '
        f'{source}')

with open("hello.txt", "a") as f:
    output = (f'{efficiency_symbol:{max_pad_efficiency}}'
            f' {english:{max_pad_english}} '
            f'{suggestions} < {stroked}  '
            f'{source}')
    newline = "\n"
    f.write(f"{output}{newline}")
    f.flush()
