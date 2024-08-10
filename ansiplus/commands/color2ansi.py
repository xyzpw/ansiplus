from ansiplus.ansi.colors import *

__all__ = [
    "foreground",
    "background",
]

def foreground(color: str|int|tuple) -> str:
    isHex = str(color).startswith("#") and len(color) in [3+1, 6+1]
    if isinstance(color, str):
        if isHex:
            return fromhex(color)
        color = color.upper()
        for k,v in vars(Fore).items():
            if k == color:
                return v
    elif isinstance(color, int):
        if color in range(0, 256):
            return fromid(color)
    elif isinstance(color, tuple):
        return from_rgb(color)

def background(color: str|int|tuple) -> str:
    isHex = str(color).startswith("#") and len(color) in [3+1, 6+1]
    if isinstance(color, str):
        if isHex:
            return fromhex(color, "background")
        color = color.upper()
        for k,v in vars(Back).items():
            if k == color:
                return v
    elif isinstance(color, int):
        if color in range(0, 256):
            return fromid(color, "background")
    elif isinstance(color, tuple):
        return from_rgb(color, "background")
