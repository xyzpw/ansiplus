from ansiplus.commands import color2ansi

__all__ = [
     "colorize",
]

def colorize(text: str, color: str|int|tuple = None, bgcolor: str|int|tuple = None) -> str:
    """Returns the given text wrapped inside the specified colors ANSI code.

    :param text:    the text to wrap in color ANSI codes
    :param color:   the foreground color of which ANSI's code will wrap the given text
    :param bgcolor: the background color of which ANSI's code will wrap the given text
    """
    if color != None:
        text = color2ansi.foreground(color) + text + color2ansi.foreground("RESET")
    if bgcolor != None:
            text = color2ansi.background(bgcolor) + text + color2ansi.background("RESET")
    return text
