from ansiplus.ansi import styles
from ansiplus.ansi.colors import Fore, Back

def validateStyle(style: str) -> tuple:
    if style == None: style = ""
    if not isinstance(style, str):
        raise TypeError("'style' must be type string")
    style = style.lower()
    match style:
        case "":
            pass
        case "bold":
            return styles.BOLD, styles.BOLD_RESET
        case "dim":
            return styles.DIM, styles.DIM_RESET
        case "italic":
            return styles.ITALIC, styles.ITALIC_RESET
        case "underline":
            return styles.UNDERLINE, styles.UNDERLINE_RESET
        case "blinking":
            return styles.BLINKING, styles.BLINKING_RESET
        case "inverse_color":
            return styles.INVERSE_COLOR, styles.INVERSE_COLOR_RESET
        case "hidden_text":
            return styles.HIDDEN_TEXT, styles.HIDDEN_TEXT_RESET
        case "strikethrough":
            return styles.STRIKETHROUGH, styles.STRIKETHROUGH_RESET
        case _:
            raise ValueError("style not found")

def getColorList() -> dict:
    colorList = {}
    for c in vars(Fore):
        if not c.startswith("__"):
            colorList[c] = vars(Fore)[c]
    return colorList
def getBackgroundColorList() -> dict:
    bgColorList = {}
    for c in vars(Back):
        if not c.startswith("__"):
            bgColorList[c] = vars(Back)[c]
    return bgColorList

def getTextStyles() -> dict:
    textStyleList = {}
    for s in vars(styles.TEXT_STYLES):
        if not s.startswith("__"):
            textStyleList[s] = vars(styles.TEXT_STYLES)[s]
    return textStyleList

def validateRGB(rgb: tuple) -> bool:
    if not isinstance(rgb, tuple):
        return False
    if len(rgb) != 3:
        return False
    for val in rgb:
        if not isinstance(val, int):
            return False
        elif not val in range(0, 255+1):
            return False
    return True

def validateColorList(color: str|int) -> bool:
    if isinstance(color, int):
        if color in range(0, 256):
            return True
    if not isinstance(color, str):
        return False
    elif color.upper() not in getColorList():
        return False
    return True

def validateBackgroundColorList(color: str|int) -> bool:
    if isinstance(color, int):
        if color in range(0, 256):
            return True
    if not isinstance(color, str):
        return False
    elif color.upper() not in getBackgroundColorList():
        return False
    return True

def validateColor(color: str|int|tuple, view: str = "foreground"):
    if isinstance(color, int):
        if color in range(0, 256):
            return True
        return False
    view = view.lower()
    match view:
        case "foreground" | "fore":
            if isinstance(color, tuple):
                return validateRGB(color)
            return validateColorList(color)
        case "background" | "back":
            if isinstance(color, tuple):
                return validateRGB(color)
            return validateBackgroundColorList(color)
    return False
