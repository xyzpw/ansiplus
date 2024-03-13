
if __name__ == "__main__":
    import ansiplus
    print("print_color: ", end='')
    ansiplus.print_color("red example", "red")
    print("print_color: ", end='')
    ansiplus.print_color("red example", bgcolor="red")
    print("print_rgb:   ", end='')
    ansiplus.print_rgb("rgb example (200, 100, 50)", (200, 100, 50))
    print("print_rgb:   ", end='')
    ansiplus.print_rgb("rgb example (200, 100, 50)", bg_rgb=(200, 100, 50))
    styleList = [
        'bold', 'dim',
        'italic', 'underline',
        'blinking', 'inverse_color',
        'hidden_text', 'strikethrough',
    ]
    print("\n")
    for s in styleList:
        if s == "blinking":
            print("this following text should be blinking: ", end='')
        elif s == "hidden_text":
            print("this following text should not be visible: ", end='')
        else:
            print("print_style: ", end='')
        ansiplus.print_style(s, style=s)
