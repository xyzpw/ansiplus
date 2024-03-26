
if __name__ == "__main__":
    from ansiplus import NewPrompt
    ui = NewPrompt()
    ui.set_color(197)
    ui.set_prompt_color(203)
    print("ctrl+c to exit\n")
    while True:
        try:
            ui.prompt("input text: ", clearline=True)
        except (KeyboardInterrupt, EOFError):
            raise SystemExit(0)
