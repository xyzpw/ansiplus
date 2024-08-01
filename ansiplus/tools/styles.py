
if __name__ == "__main__":
    from ansiplus import *
    print("print_color: ", end='')
    print_color("red example", "red")
    print("print_color: ", end='')
    print_color("red example", bgcolor="red")
    print("print_color: ", end='')
    print_color("rgb example (200, 100, 50)", (200, 100, 50))
    print("print_color: ", end='')
    print_color("rgb example (200, 100, 50)", bgcolor=(200, 100, 50))
    print("print_color: ", end='')
    print_color("rainbow example", "rainbow")
    print("print_color: ", end='')
    print_color("random example", "random")
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
        print_style(s, style=s)
