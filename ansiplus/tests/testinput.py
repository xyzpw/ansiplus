
if __name__ == "__main__":
    from ansiplus import NewPrompt
    ui = NewPrompt()
    ui.prompt("colored input test (green): ", "green", clearline=True)
    ui.prompt("colored prompt test (red): ", prompt_color="red", clearline=True)
    ui.prompt("colored prompt test (rainbow): ", prompt_color="rainbow", clearline=True)
    ui.prompt("colored prompt test (random): ", prompt_color="random", clearline=True)
    print("Your input history:", ", ".join(ui.history))
