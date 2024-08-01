
if __name__ == "__main__":
    from ansiplus.uiHandler.validateinput import getColorList, getBackgroundColorList
    colorList = getColorList()
    bgColorList = getBackgroundColorList()
    for col in colorList:
        if col != "RESET":
            print(f"{colorList[col]}{col}{colorList['RESET']}")
    print("\n", end='')
    for bc in bgColorList:
        if bc != "RESET":
            print(f"{bc} {bgColorList[bc]}{' '*8}{bgColorList['RESET']}")

