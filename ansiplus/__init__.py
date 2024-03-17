"""
A Python package designed to enhance code readability and CLI experience.
"""

ESC = "\x1b"
from .commands.colortext import colorize, colorizeRGB
from .commands.styletext import stylize_text
from .commands.cursorcontrols import *
import ansiplus.ansi.colors, ansiplus.ansi.cursor, ansiplus.ansi.erase, ansiplus.ansi.styles

__version__ = "1.1.0"
__author__ = "xyzpw"
__description__ = "A Python package designed to enhance code readability and CLI experience."

def set_color(color: str|int = None, bgcolor: str|int = None):
    """Sets the color of text permanently or until reset.

    :param color:   the foreground color that will be used on text
    :param bgcolor: the background color that will be used on text
    """
    from ansiplus.uiHandler.validateinput import getColorList, validateColorList, getBackgroundColorList
    colorList = getColorList()
    bgColorList = getBackgroundColorList()
    hasFG = validateColorList(color)
    hasBG = validateColorList(bgcolor)
    if hasFG:
        if isinstance(color, int):
            print(ansiplus.ansi.colors.fromid(color, "foreground"), end='')
        elif isinstance(color, str):
            print(colorList[color.upper()], end='')
    if hasBG:
        if isinstance(bgcolor, int):
            print(ansiplus.ansi.colors.fromid(bgcolor, "background"), end='')
        elif isinstance(bgcolor, str):
            print(bgColorList[bgcolor.upper()], end='')

def print_color(text: str, color: str|int = None, bgcolor: str|int = None):
    """Prints colored text.

    :param text:    the text that will be colored and printed
    :param color:   the foreground color of the text to be printed
    :param bgcolor: the background color of the text to be printed
    """
    print(colorize(text, color, bgcolor))

def input_color(text: str = "", color: str|int = None, revert_color: str|int = 'RESET') -> str:
    """Changes the foreground color of prompt input text.

    :param text:         the prompt text to be displayed
    :param color:        the foreground color to use on prompt input text
    :param revert_color: the color to revert to after the prompt is complete
    """
    from ansiplus.uiHandler.validateinput import getColorList, validateColorList
    colorList = getColorList()
    if not validateColorList(color):
        raise ValueError("color does not exist")
    if bool(revert_color):
        if not validateColorList(color):
            raise ValueError("reset color does not exist")
    if isinstance(color, int):
        out = input(text + ansiplus.ansi.colors.fromid(color))
    elif isinstance(color, str):
        out = input(text + colorList[color.upper()])
    if revert_color != False:
        if isinstance(revert_color, int):
            print(ansiplus.ansi.colors.fromid(revert_color), end='')
        elif isinstance(revert_color, str):
            print(colorList[revert_color.upper()], end='')
    return out

class NewPrompt:
    def __init__(self):
        self.color = "RESET"
        self.revert_color = "RESET"
        self.history = []
        self.latest = ""
    def prompt(self, text: str = "", color: str|int = None, revert_color: str|int = None) -> str:
        workingColor = color if bool(color) else self.color
        workingRevertColor = revert_color if bool(revert_color) else self.revert_color
        _out = input_color(text, workingColor, workingRevertColor)
        self.history.append(_out)
        self.latest = _out
        return _out
    def clear_history(self):
        self.history = []
        self.latest = None
    def set_color(self, color: str, revert_color: str|int = "RESET") -> str:
        self.color = color
        self.revert_color = revert_color

def print_style(text: str, style: str):
    """Prints text with the style specified.

    :param text:  the text that will be stylized
    :param style: the style to use for the given text
    """
    print(stylize_text(text, style))

def print_rgb(text: str, rgb: tuple = (), bg_rgb: tuple = ()):
    """Prints text in the color of the given RGB code.

    :param text:    the foreground RGB color that will be used on the printed text
    :param bgcolor: the background RGB color that will be used on the printed text
    """
    print(colorizeRGB(text, rgb, bg_rgb))

def save_cursor_position():
    """Saves the cursor position."""
    print(ansiplus.ansi.cursor.SAVE_POSITION, end='')

def restore_cursor_position():
    """Restores cursor to the last saved position."""
    print(ansiplus.ansi.cursor.RESTORE_POSITION, end='')

def move_cursor(direction: str, no: int = 1):
    """Moves the cursor up, down, right, and left by a specified distance.
    Optionally, you can move the cursor to the home position (0, 0).
    Setting the cursor position to "home" will render the 'no' argument ineffective.

    :param direction: the direction of which the cursor will move to
    :param no:        the number of column/rows the cursor will move
    """
    if no < 0:
        raise ValueError("line numbers must be a positive value")
    match direction:
        case "up":
            print(cursor_up(no), end='')
        case "down":
            print(cursor_down(no), end='')
        case "right":
            print(cursor_right(no), end='')
        case "left":
            print(cursor_left(no), end='')
        case "home":
            # the `no` arg has no effect on this option
            print(ansiplus.ansi.cursor.HOME, end='')

def set_cursor_position(row: int, column: int):
    """Moves the cursor to a specific position according to the specified row and column."""
    if not isinstance(row, int) or not isinstance(column, int):
        raise TypeError("row and column values must be integers")
    print(ansiplus.ansi.cursor.set_position(row, column), end='')

def set_cursor_visibility(visible: bool):
    """Makes the cursor visible or invisible.

    :param state: the state of the cursor, true for visible, false for invisible
    """
    if not isinstance(visible, bool):
        raise TypeError("cursor visibility must be type boolean")
    if visible:
        print(ansiplus.ansi.cursor.VISIBLE, end='')
    elif not visible:
        print(ansiplus.ansi.cursor.INVISIBLE, end='')

def erase_row(no: int = 0):
    """Clears specified row number.
    Setting the 'no' parameter to a negative value will move the position down in contrast to up.

    :param no: the above line of which will be cleared (can be negative)
    """
    if not isinstance(no, int):
        raise TypeError("row number must be an integer")
    if no > 0:
        print(ansiplus.ansi.cursor.cursor_up(no), end='')
        print(ansiplus.ansi.erase.LINE, end='')
        print(ansiplus.ansi.cursor.cursor_down(no), end='')
    if no < 0:
        print(ansiplus.ansi.cursor.cursor_down(abs(no)), end='')
        print(ansiplus.ansi.erase.LINE, end='')
        print(ansiplus.ansi.cursor.cursor_up(abs(no)), end='')
    if no == 0:
        print(ansiplus.ansi.erase.LINE, end='')

def clear_screen(clear_type: str = "all"):
    """Clears the screen with ANSI codes.

    :clear_type all:             moves cursor to home position prior to clearing screen
    :clear_type screen:          clears entire screen while keeping cursor position
    :clear_type bottom:          clears from from cursor to bottom
    :clear_type top:             clears from cursor to top
    :clear_type buffer:          clears all saved lines and will prevent scrollback
    :clear_type cursorToLineEnd: clears the entire line starting from cursor
    :clear_type lineToCursor:    clears line text behind the cursor
    :clear_type line:            clears the entire line
    """
    match clear_type:
        case "all":
            print(ansiplus.ansi.erase.ALL, end='')
        case "screen":
            print(ansiplus.ansi.erase.SCREEN, end='')
        case "bottom":
            print(ansiplus.ansi.erase.BOTTOM_SCREEN, end='')
        case "top":
            print(ansiplus.ansi.erase.TOP_SCREEN, end='')
        case "buffer" | "saved":
            print(ansiplus.ansi.erase.BUFFER, end='')
        case "cursorToLineEnd" | "cursor_to_line_end" | "cursor-to-line-end":
            print(ansiplus.ansi.erase.CURSOR_TO_LINE_END, end='')
        case "lineToCursor" | "line_to_cursor" | "line-to-cursor":
            print(ansiplus.ansi.erase.LINE_TO_CURSOR, end='')
        case "line":
            print(ansiplus.ansi.erase.LINE, end='')

def reset_colors_and_styles():
    """Resets all colors and styles."""
    print(ESC + "[0m", end='')
