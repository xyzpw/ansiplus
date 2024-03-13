from ansiplus import ESC

INVISIBLE = ESC + "[?25l"
VISIBLE = ESC + "[?25h"
HOME = ESC + "[H"
SAVE_POSITION = ESC + "[s"
RESTORE_POSITION = ESC + "[u"

def cursor_up(no: int = 1) -> str:
    """Returns the ANSI code which moves the cursor # rows up."""
    return ESC + f"[{no}A"

def cursor_down(no: int = 1) -> str:
    """Returns the ANSI code which moves the cursor # rows down."""
    return ESC + f"[{no}B"

def cursor_right(no: int = 1) -> str:
    """Returns the ANSI code which moves the cursor # columns to the right."""
    return ESC + f"[{no}C"

def cursor_left(no: int = 1) -> str:
    """Returns the ANSI code which moves the cursor # columns to the left."""
    return ESC + f"[{no}D"

def set_position(row: int, column: int) -> str:
    """Returns the ANSI code which moves the cursor to the specified coordinates."""
    return ESC + f"[{row};{column}f" #NOTE: the 'f' can be replaced with 'H'
