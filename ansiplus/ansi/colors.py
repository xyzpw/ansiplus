from ansiplus import ESC

__all__ = [
    "Fore",
    "Back",
    "from_rgb",
    "fromid",
]

#NOTE: RESET and DEFAULT are the same
class Fore:
    BLACK = ESC + "[30m"
    RED = ESC + "[31m"
    GREEN = ESC + "[32m"
    YELLOW = ESC + "[33m"
    BLUE = ESC + "[34m"
    MAGENTA = ESC + "[35m"
    CYAN = ESC + "[36m"
    WHITE = ESC + "[37m"
    BRIGHT_BLACK = ESC + "[90m"
    BRIGHT_RED = ESC + "[91m"
    BRIGHT_GREEN = ESC + "[92m"
    BRIGHT_YELLOW = ESC + "[93m"
    BRIGHT_BLUE = ESC + "[94m"
    BRIGHT_MAGENTA = ESC + "[95m"
    BRIGHT_CYAN = ESC + "[96m"
    BRIGHT_WHITE = ESC + "[97m"
    RESET = ESC + "[39m"
    DEFAULT = ESC + "[39m"

class Back:
    BLACK = ESC + "[40m"
    RED = ESC + "[41m"
    GREEN = ESC + "[42m"
    YELLOW = ESC + "[43m"
    BLUE = ESC + "[44m"
    MAGENTA = ESC + "[45m"
    CYAN = ESC + "[46m"
    WHITE = ESC + "[47m"
    BRIGHT_BLACK = ESC + "[100m"
    BRIGHT_RED = ESC + "[101m"
    BRIGHT_GREEN = ESC + "[102m"
    BRIGHT_YELLOW = ESC + "[103m"
    BRIGHT_BLUE = ESC + "[104m"
    BRIGHT_MAGENTA = ESC + "[105m"
    BRIGHT_CYAN = ESC + "[106m"
    BRIGHT_WHITE = ESC + "[107m"
    RESET = ESC + "[49m"
    DEFAULT = ESC + "[49m"

def from_rgb(rgb: tuple, position: str = "foreground"):
    r, g, b = rgb[0], rgb[1], rgb[2]
    if position.lower() in ["fore", "foreground"]:
        return ESC + f"[38;2;{r};{g};{b}m"
    elif position.lower() in ["back", "background"]:
        return ESC + f"[48;2;{r};{g};{b}m"

def fromid(colorid: int, position: str = "foreground"):
    if position.lower() in ["fore", "foreground"]:
        return ESC + f"[38;5;{colorid}m"
    elif position.lower() in ["back", "background"]:
        return ESC + f"[48;5;{colorid}m"
