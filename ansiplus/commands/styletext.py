from ansiplus.uiHandler.validateinput import validateStyle

__all__ = [
    "stylize_text",
]

def stylize_text(text: str, style: str) -> str:
    """Stylizes the given text.

    :param text:  the text to stylize
    :param style: the style which will be used on the given text
    """
    styleCode, styleResetCode = validateStyle(style)[0], validateStyle(style)[1]
    out = f"{styleCode}{text}{styleResetCode}"
    return out
