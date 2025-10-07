from string import punctuation

whole_text = []
with open("text.txt") as file:
    for i, line in enumerate(file):
        alnum_chars_count = len([char for char in line if char.isalnum()])
        special_chars_count = len([char for char in line if char in punctuation])
        line_n = i + 1
        whole_text.append(f"Line {line_n}: {line.strip()} ({alnum_chars_count})({special_chars_count})")

with open("output.txt", "w") as file:
    file.write("\n".join(whole_text))
