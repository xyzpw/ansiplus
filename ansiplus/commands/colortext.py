from ansiplus.commands import color2ansi
from random import randint

__all__ = [
    "colorize",
    "makeRainbow",
    "randomizeCharColors",
]


def randomizeCharColors(text: str) -> str:
    rainbowText = ""
    for c in list(text):
        if c == " ":
            rainbowText += c
            continue
        rainbowText += color2ansi.foreground(randint(0, 255)) + c + color2ansi.foreground("RESET")
    return rainbowText

#NOTE: rainbow
# red -> 255, 0, 0
# orange -> 255, 165, 0
# yellow -> 255, 255, 0
# green -> 0, 255, 0
# blue -> 0, 0, 255
# indigo -> 51, 0, 153
# violet -> 143, 0, 255

def makeRainbow(text: str) -> str:
    rainbowColors = [
        (255, 0, 0),
        (255, 165, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 0, 255),
        (51, 0, 153),
        (143, 0, 255),
    ]
    rainbowText = ''
    textList = list(text)
    for i in range(len(textList)):
        if textList[i] == " ":
            rainbowText += textList[i]
            continue
        iterColor = rainbowColors[i%(len(rainbowColors)-1)]
        rainbowText += color2ansi.foreground(iterColor) + textList[i] + color2ansi.foreground("RESET")
    return rainbowText

def colorize(text: str, color: str|int|tuple = None, bgcolor: str|int|tuple = None) -> str:
    """Returns the given text wrapped inside the specified colors ANSI code.

    :param text:    the text to wrap in color ANSI codes
    :param color:   the foreground color of which ANSI's code will wrap the given text
    :param bgcolor: the background color of which ANSI's code will wrap the given text
    """
    if str(color).lower() == "rainbow":
        text = makeRainbow(text)
    elif str(color).lower() == "random":
        text = randomizeCharColors(text)
    elif color != None:
        text = color2ansi.foreground(color) + text + color2ansi.foreground("RESET")
    if bgcolor != None:
        text = color2ansi.background(bgcolor) + text + color2ansi.background("RESET")
    return text
