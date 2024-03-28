# ansiplus
![Pepy Total Downlods](https://img.shields.io/pepy/dt/ansiplus?color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiplus)
![GitHub repo size](https://img.shields.io/github/repo-size/xyzpw/ansiplus)
![PyPI - License](https://img.shields.io/pypi/l/ansiplus)
![PyPI - Version](https://img.shields.io/pypi/v/ansiplus)

A Python package designed to enhance code readability and CLI experience.

![ansiplus-v2_1-preview](https://github.com/xyzpw/ansiplus/assets/76017734/4078141f-578e-443c-aec9-d08110f5f5e9)


## Usage
> [!WARNING]
> Not all terminals work perfectly with ANSI codes.
> Ideally you should use xterm-256color.

> [!NOTE]
> Terminal themes can change colors, e.g. magenta might show up as yellow, but it is still using the magenta ANSI code.

### Prerequisites
- Python version >=3.10
- A terminal emulator that accepts ANSI codes
- A terminal emulator that uses xterm-256color

> [!NOTE]
> ANSi codes are not limited to xterm-256color, but they may still be limited to all features this package provides.

#### Tested Terminals on Linux
Terminal ($TERM)
- Konsole (xterm-256color) - no missing features
- Xterm (xterm) - no missing features
- Alacritty (alacritty) - blinking text does not work
- Kitty (xterm-kitty) - blinking text does not work

### Colors
This package introduces the ability to print colors via name, id, and rgb with a single function:
```python
>>> from ansiplus import print_color
>>> print_color("my colored text", color=(100, 200, 255), bgcolor=198)
'my colored text'
>>> print_color("red text", color="red")
```

Colors may also be manually printed:
```python
>>> from ansiplus.ansi.colors import Fore
>>> print(f"{Fore.GREEN}green text{Fore.RESET}")
```

#### Rainbow & Random Colors
Text can be colored to resemble a rainbow:
```python
>>> from ansiplus import print_color
>>> print_color("this text is rainbow colored", "rainbow")
'this text is rainbow colored'
>>> print_color("each character will be a random color", "random")
'each character will be a random color'
```

> [!WARNING]
> Using rainbow or random color option uses a lot of ANSI codes.

### User Input
Along with colors, users can be prompted for input which can be colored:
```python
>>> from ansiplus import input_color
>>> txt = input_color("example: ", color="blue")
>>> print(txt)
'my input'
```

Prompting input can also store history if you assign it to a variable:
```python
>>> from ansiplus import NewPrompt
>>> ui = NewPrompt()
>>> ui.set_color("red")
>>> ui.set_prompt_color("green")
>>> ui.prompt("prompt class example: ")
>>> ui.history
['my text']
>>> ui.latest
'my text'
>>> ui.prompt("prompt class example 2: ", "yellow")
>>> ui.latest
'this text is yellow, but default is red'
```

#### Rainbow & Random Colors
Prompt foreground text can also be colored rainbow:
```python
>>> from ansiplus import input_color
>>> input_color("this text is rainbow: ", prompt_color="rainbow")
```

#### Clearing Prompt Lines
After receiving user input, the line can be cleared:
```python
from ansiplus import input_color
while True:
    input_color("forever input: ", clearline=True)
```
The above code sample will ask for input forever, after every input, the line will clear and the input will be prompted again on the same line.

### Text Styles
This package includes several several styles that can be used:
```python
>>> from ansiplus import print_style
>>> print_style("underline text", "underline")
'underline text'
```

Like colors, styles may also be used manually:
```python
>>> from ansiplus.ansi.styles import BOLD, BOLD_RESET
>>> print(f"{BOLD}bold text{BOLD_RESET}")
'bold text'
>>>
```

### More Functions
There are more ANSI codes featured beyond colors and styles, these could be viewed by using `help(ansiplus)` inside the python interpreter.

## Developers
When building the package for testing, it is recommended to use `python3 -m build`.
### Wheels
When building the package for testing, it is recommended to use `python3 -m build`.
### PIP Virtual Environments
Virtual environments should be named ".venv" or ".env", as this is used in the ".gitignore" file.

### Contributing
Contributions must not include:
- breaking code
- major changes
- changes to the version number
- wheel files or egg-info files
- spaghetti code
