edited_text = []
special_chars = ["-", ",", ".", "!", "?"]

with open("text.txt") as f:
    for i, line in enumerate(f):
        if i % 2 == 0:
            # changing special chars to '@'
            line = [char if char not in special_chars else "@" for char in line]
            words_in_line = "".join(line).split()
            line_to_add = " ".join(reversed(words_in_line))
            edited_text.append(line_to_add)

with open("output.txt", "w") as f:
    f.write("\n".join(edited_text))

