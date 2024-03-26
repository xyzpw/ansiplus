from ansiplus.ansi.colors import *

__all__ = [
    "foreground",
    "background",
]

def foreground(color: str|int|tuple) -> str:
    if isinstance(color, str):
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
    if isinstance(color, str):
        color = color.upper()
        for k,v in vars(Back).items():
            if k == color:
                return v
    elif isinstance(color, int):
        if color in range(0, 256):
            return fromid(color, "background")
    elif isinstance(color, tuple):
        return from_rgb(color, "background")
