from ansiplus import ESC

BOTTOM_SCREEN = ESC + "[0J"
TOP_SCREEN = ESC + "[1J"
SCREEN = ESC + "[2J"
BUFFER = ESC + "[3J" #clears saved lines
LINE = ESC + "[2K"
CURSOR_TO_LINE_END = ESC + "[0K"
LINE_TO_CURSOR = ESC + "[1K"
ALL = ESC + "[H" + ESC + "[2J" + ESC + "[3J"