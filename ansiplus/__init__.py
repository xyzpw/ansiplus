"""
A Python package designed to enhance code readability and CLI experience.
"""

ESC = "\x1b"
from . import commands
from .commands import color2ansi
from ansiplus.commands.colortext import *
from ansiplus.commands.styletext import *
from ansiplus.commands.cursorcontrols import *
import ansiplus.ansi.colors, ansiplus.ansi.cursor, ansiplus.ansi.erase, ansiplus.ansi.styles

__version__ = "2.1"
__author__ = "xyzpw"
__description__ = "A Python package designed to enhance code readability and CLI experience."
__license__ = "MIT"

__all__ = [
    "set_color",
    "print_color",
    "input_color",
    "NewPrompt",
    "print_style",
    "save_cursor_position",
    "restore_cursor_position",
    "move_cursor",
    "set_cursor_position",
    "set_cursor_visibility",
    "erase_row",
    "clear_screen",
    "reset_colors_and_styles",
]

def set_color(color: str|int|tuple = None, bgcolor: str|int|tuple = None):
    """Sets the color of text permanently or until reset.

    :param color:   the foreground color to be used
    :param bgcolor: the background color to be used
    """
    if color != None:
        print(commands.color2ansi.foreground(color), end='')
    if bgcolor != None:
        print(commands.color2ansi.background(bgcolor), end='')


def print_color(text: str, color: str|int|tuple = None, bgcolor: str|int|tuple = None):
    """Prints colored text.

    :param text:    the text that will be colored and printed
    :param color:   the foreground color of the text to be printed
    :param bgcolor: the background color of the text to be printed
    """
    print(colorize(text, color, bgcolor))

def input_color(text: str = "", color: str|int = "RESET", revert_color: str|int = 'RESET',
    prompt_color: str|int = "RESET", prompt_revert_color: str|int = "RESET", clearline: bool = False) -> str:
    """Changes the foreground color of prompt input text.

    :param text:                the prompt text to be displayed
    :param color:               the foreground color to use on prompt input text
    :param revert_color:        the color to revert to after the prompt is complete
    :param prompt_color:        color of prompt text
    :param revert_prompt_color: the color to revert the prompt text after input has been given
    """
    from ansiplus.utils import promptColorer
    cursor, erase = ansiplus.ansi.cursor, ansiplus.ansi.erase
    text = promptColorer.colorizePrompt(text, prompt_color, prompt_revert_color)
    out = input(text + commands.color2ansi.foreground(color))
    print(commands.color2ansi.foreground(revert_color), end='')
    if clearline:
        print(f"{cursor.cursor_up(1)}{erase.LINE}", end='')
    return out

class NewPrompt:
    def __init__(self):
        self.color = "RESET"
        self.revert_color = "RESET"
        self.prompt_color = "DEFAULT"
        self.prompt_revert_color = "DEFAULT"
        self.history = []
        self.latest = ""
    def prompt(self, text: str = "", color: str|int|tuple = None, revert_color: str|int|tuple = None,
            prompt_color: str|int|tuple = None, prompt_revert_color: str|int|tuple = None, clearline: bool = False) -> str:
        workingColor = color if bool(color) else self.color
        workingRevertColor = revert_color if bool(revert_color) else self.revert_color
        workingPromptColor = prompt_color if bool(prompt_color) else self.prompt_color
        workingPromptRevertColor = prompt_revert_color if bool(prompt_revert_color) else self.prompt_revert_color
        _out = input_color(text, workingColor, workingRevertColor, workingPromptColor, workingPromptRevertColor, clearline)
        self.history.append(_out)
        self.latest = _out
        return _out
    def clear_history(self):
        self.history = []
        self.latest = None
    def set_color(self, color: str|int|tuple, revert_color: str|int|tuple = "RESET"):
        self.color = color
        self.revert_color = revert_color
    def set_prompt_color(self, color: str|int|tuple, revert_color: str|int|tuple = "RESET"):
        self.prompt_color = color
        self.prompt_revert_color = revert_color

def print_style(text: str, style: str):
    """Prints text with the style specified.

    :param text:  the text that will be stylized
    :param style: the style to use for the given text
    """
    print(stylize_text(text, style))

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
    erase = ansiplus.ansi.erase
    match clear_type:
        case "all":
            print(erase.ALL, end='')
        case "screen":
            print(erase.SCREEN, end='')
        case "bottom":
            print(erase.BOTTOM_SCREEN, end='')
        case "top":
            print(erase.TOP_SCREEN, end='')
        case "buffer" | "saved":
            print(erase.BUFFER, end='')
        case "cursorToLineEnd" | "cursor_to_line_end" | "cursor-to-line-end":
            print(erase.CURSOR_TO_LINE_END, end='')
        case "lineToCursor" | "line_to_cursor" | "line-to-cursor":
            print(erase.LINE_TO_CURSOR, end='')
        case "line":
            print(erase.LINE, end='')

def reset_colors_and_styles():
    """Resets all colors and styles."""
    print(ESC + "[0m", end='')
