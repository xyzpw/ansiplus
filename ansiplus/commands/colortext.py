from ansiplus.ansi.colors import Fore, Back, fromid, from_rgb
from ansiplus.uiHandler.validateinput import getColorList, getBackgroundColorList, validateRGB, validateColorList, validateBackgroundColorList

def colorize(text: str, color: str|int = None, bgcolor: str|int = None) -> str:
    """Returns the given text wrapped inside the specified colors ANSI code.

    :param text:    the text to wrap in color ANSI codes
    :param color:   the foreground color of which ANSI's code will wrap the given text
    :param bgcolor: the background color of which ANSI's code will wrap the given text
    """
    if isinstance(color, str):
        color = color.upper()
    if isinstance(bgcolor, str):
        bgcolor = bgcolor.upper()
    colorList = getColorList()
    bgColorList = getBackgroundColorList()
    if color != None:
        if not validateColorList(color):
            raise ValueError("invalid color")
    if bgcolor != None:
        if not validateBackgroundColorList(bgcolor):
            raise ValueError("invalid background color")
    out = ""
    if color != None:
        if isinstance(color, int):
            out += f"{fromid(color)}{text}{Fore.RESET}"
        elif isinstance(color, str):
            out += f"{colorList[color]}{text}{Fore.RESET}"
    if bgcolor != None:
        if not bool(color):
            if isinstance(bgcolor, int):
                out = f"{fromid(bgcolor, 'background')}{text}{Back.RESET}"
            elif isinstance(bgcolor, str):
                out = f"{bgColorList[bgcolor]}{text}{Back.RESET}"
        else:
            if isinstance(bgcolor, int):
                out = f"{fromid(bgcolor, 'background')}{out}{Back.RESET}"
            else:
                out = f"{bgColorList[bgcolor]}{out}{Back.RESET}"
    return out

def colorizeRGB(text: str, color: tuple = (), bgcolor: tuple = ()) -> str:
    """Returns the text wrapped inside RGB ANSI codes.

    :param text:    the text that will be wrapped inside ANSI codes
    :param color:   the foreground RGB values of which ANSI codes will wrap the given text
    :param bgcolor: the background RGB values of which ANSI codes will wrap the given text
    """
    if not isinstance(color, tuple) or not isinstance(bgcolor, tuple):
        raise TypeError("colors must be type tuple")
    hasFG = validateRGB(color)
    hasBG = validateRGB(bgcolor)
    out = ""
    if hasFG:
        out += f"{from_rgb(color)}{text}{Fore.RESET}"
    if hasBG:
        if not hasFG:
            out = f"{from_rgb(bgcolor, 'background')}{text}{Back.RESET}"
        else:
            out = f"{from_rgb(bgcolor, 'background')}{out}{Back.RESET}"
    return out
