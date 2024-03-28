from ansiplus.commands import color2ansi, colortext
from . import validatecolors

def colorizePrompt(text: str, color="DEFAULT", revert_color="DEFAULT") -> str:
    if color in ["rainbow", "random"]:
        text = colortext.colorize(text, color) + color2ansi.foreground(revert_color)
    else:
        if not validatecolors.validate([color, revert_color]):
            raise ValueError("invalid colors")
        text = color2ansi.foreground(color) + text + color2ansi.foreground(revert_color)
    return text
