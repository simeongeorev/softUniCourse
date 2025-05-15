first_string = input()
second_string = input()

word_length = len(first_string)

if word_length == 1:
    print(second_string)

for i in range(word_length):
    char = second_string[i]
    if first_string[i] != second_string[i]:
        holder_string = second_string[:i+1] + first_string[i + 1:word_length]
        print(holder_string)

