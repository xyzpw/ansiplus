from ansiplus.uiHandler.validateinput import validateColor

def validate(colors: list, view: str = "foreground") -> bool:
    for color in colors:
        if not validateColor(color, view):
            return False
    return True
