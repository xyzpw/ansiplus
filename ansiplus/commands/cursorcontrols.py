from ansiplus import ESC

__all__ = [
    "cursor_up",
    "cursor_down",
    "cursor_right",
    "cursor_left",
]

def cursor_up(no: int) -> str:
    """Moves the cursor # lines up."""
    return ESC + f"[{no}A"

def cursor_down(no: int) -> str:
    """Moves the cursor # lines down."""
    return ESC + f"[{no}B"

def cursor_right(no: int) -> str:
    """Moves the cursor # columns right."""
    return ESC + f"[{no}C"

def cursor_left(no: int) -> str:
    """Moves the cursor # columns right."""
    return ESC + f"[{no}D"
