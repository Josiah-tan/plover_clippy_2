
def hex2Rgb(rgb):
    if type(rgb) == str:
        rgb = int(rgb, 16)
    return ((rgb >> 16) & 0xff, (rgb >> 8) & 0xff, rgb & 0xff)


def getStandardAnsi(value):
    if type(value) == int:  # ansi
        return f"\033[38;5;{value}m"
    elif (value[0] == "#" and
            len(value) == 7):  # hex
        red, green, blue = hex2Rgb(value[1:])
        return f"\033[38;2;{red};{green};{blue}m"
    elif value[0] == "\033":  # ansi color code
        return value
    else:
        raise ValueError(f"invalid input: {value}")


def wrapAnsi(color, string):
    return color+string+"\u001b[0m"
