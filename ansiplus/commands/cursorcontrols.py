from ansiplus import ESC

__all__ = [
    "cursor_up",
    "cursor_down",
    "cursor_right",
    "cursor_left",
]

def cursor_up(no: int) -> str:
    """Returns the ANSI code which moves the cursor # rows up."""
    return ESC + f"[{no}A"

def cursor_down(no: int) -> str:
    """Returns the ANSI code which moves the cursor # rows down."""
    return ESC + f"[{no}B"

def cursor_right(no: int) -> str:
    """Returns the ANSI code which moves the cursor # columns to the right."""
    return ESC + f"[{no}C"

def cursor_left(no: int) -> str:
    """Returns the ANSI code which moves the cursor # columns to the left."""
    return ESC + f"[{no}D"
