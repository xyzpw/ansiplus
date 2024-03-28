# Changelog

## v2.1 (2024-03-28)

### Added
- Foreground colors:
  - rainbow: resembles the colors of a rainbow
  - random: assigns a random color to each character

### Changed
- tests: prompt text for colored input

### Bug Fixes
- inability to validate prompt color

## v2.0 - 2024-03-26

### Added
- ability to color prompt text along with prompt input text
- ability to clear prompt line subsequent to receiving user input
- ability to convert color name to ansi code
- ability to use rgb colors with prompt inputs

### Removed
#### Functions
- print_rgb

## v1.1 - 2024-03-16

### Added
- new class for custom input prompt: `NewPrompt`
  - view prompt history
  - clear prompt history
  - use specified or set default colors
- new `clear_screen` argument option: "all"
  - relocates cursor to home position prior to clearing screen and buffer

### Changed
- changed default `clear_screen` argument from "screen" to "all"

## v1.0.1.post1 - 2024-03-13
- added url to setup.py

## v1.0.1 - 2024-03-13
- fixed import errors
