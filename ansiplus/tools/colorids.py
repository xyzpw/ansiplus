
#NOTE: for foreground: ESC[38;5;{ID}m
#NOTE: for background: ESC[48;5;{ID}m
if __name__ == "__main__":
    from ansiplus import ESC
    for i in range(256):
        print(f"{ESC}[38;5;{i}m{i}", end=' ')

