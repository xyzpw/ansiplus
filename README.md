# ansiplus
![Pepy Total Downlods](https://img.shields.io/pepy/dt/ansiplus?color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansiplus)
![GitHub repo size](https://img.shields.io/github/repo-size/xyzpw/ansiplus)
![PyPI - License](https://img.shields.io/pypi/l/ansiplus)

A Python package designed to enhance code readability and CLI experience.

![ansiplus-preview](https://github.com/xyzpw/ansiplus/assets/76017734/bf852703-e04a-444e-aa78-7bdaae98ac41)

# Usage
> [!WARNING]
> Not all terminals work perfectly with ANSI codes.
> Ideally you should use xterm-256color.

> [!NOTE]
> Terminal themes can change colors, e.g. magenta might show up as yellow, but it is still using the magenta ANSI code.

## Prerequisites
- Python version >=3.10
- A terminal emulator that accepts ANSI codes
- A terminal emulator that uses xterm-256color

> [!NOTE]
> ANSI codes aren't just limited to xterm-256color, but they may still be limited to all features this package includes.

### Tested Terminals on Linux
Terminal ($TERM)
- Konsole (xterm-256color) - no missing features
- Xterm (xterm) - no missing features
- Alacritty (alacritty) - blinking text does not work
- Kitty (xterm-kitty) - blinking text does not work

## Colors
Printing colored text can be used from a single function:
```python
>>> from ansiplus import print_color
>>> print_color(text="hello world", color="red")
hello world
>>>
```
Optionally, you can also use the `bgcolor` parameter to change the background color.<br><br>
Manually putting the color ANSI codes could be used at well:
```python
>>> from ansiplus.ansi.colors import Fore, Back
>>> Fore.RED
'\x1b[31m'
>>> Back.RED
'\x1b[41m'
>>> print(f"{Fore.RED}hello world{Fore.RESET}") #output will appear in red
hello world
>>>
```

RGB colors are also an option:
```python
>>> from ansiplus import print_rgb
>>> print_rgb(text="custom rgb text", rgb=(200, 108, 0))
custom rgb text
>>>
```

## User Input
User input during a prompt can be colored:
```python
>>> from ansiplus import input_color
>>> foo = input_color(text="name: ", color="blue") #users input will appear in blue
name:
>>>
```

## Text Styles
Text can be stylized and printed:
```python
>>> from ansiplus import print_style
>>> print_style("bold text", 'bold')
bold text
>>>
```
Like colors, this can also be done manually:
```python
>>> from ansiplus.ansi.styles import BOLD, BOLD_RESET
>>> BOLD
'\x1b[1m'
>>> BOLD_RESET
'\x1b[22m'
>>> print(f"{BOLD}bold text{BOLD_RESET}")
bold text
>>>
```

## More Functions
There are more ANSI code features beyond colors and styles, these could be viewed by using `help(ansiplus)` inside the python interpreter.

# Developers

## Building
### Wheels
When building the package for testing, it is recommended to use `python3 -m build`
### PIP Virtual Environments
Virtual environments should be named ".venv" or ".env", as this is used in the ".gitignore" file.

## Contributing
Contributions must not include:
- breaking code
- major changes
- changes to the version number
- wheel files or egg-info files
- spaghetti code

