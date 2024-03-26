
if __name__ == "__main__":
    from ansiplus import input_color
    mytext = input_color("text prompt example (green): ", "green")
    print("your text:", mytext)
    mytext = input_color("colored prompt test (red): ", prompt_color="red")
    print("your text:", mytext)
