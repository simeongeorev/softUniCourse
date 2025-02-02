word = ""
inner_word = ""
c_char_counter = 0
o_char_counter = 0
n_char_counter = 0

while True:
    char = input() # repeat the cycle

    if char == "End":
        print(word)
        break

    elif char.isalpha(): # valid latin char
        should_skip = False
        if char == "c" and c_char_counter < 1:
            c_char_counter += 1
            should_skip = True
        elif char == "o" and o_char_counter < 1:
            o_char_counter += 1
            should_skip = True
        elif char == "n" and n_char_counter < 1:
            n_char_counter += 1
            should_skip = True

        if c_char_counter == 1 and o_char_counter == 1 and n_char_counter == 1:
            word = word + inner_word + " "
            inner_word = ""
            c_char_counter = 0
            o_char_counter = 0
            n_char_counter = 0

        if should_skip:
            continue

        inner_word += char

    else: # invalid char
        continue






