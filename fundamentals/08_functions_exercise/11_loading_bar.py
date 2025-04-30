def loading_text(percentages: int):
    if percentages == 100:
        text = "100% Complete!\n[%%%%%%%%%%]"
    else:
        perc_signs = int(percentages / 10)
        loading_bar = ""
        for i in range(10):
            if i < perc_signs:
                loading_bar += "%"
            else:
                loading_bar += "."
        text = f"{percentages}% [{loading_bar}]\nStill loading..."
    return text

print(loading_text(int(input())))
