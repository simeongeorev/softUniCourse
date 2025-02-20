# # # Using string slicing - gives errors in judge, don't know why

# first_string = input()
# second_string = input()
#
# word_length = len(first_string)
#
# if word_length == 1:
#     print(second_string)
#
# for i in range(0, word_length-1):
#     char = second_string[i]
#     if first_string[i] != second_string[i]:
#         holder_string = second_string[0:i] + second_string[i] + first_string[i + 1:word_length]
#         print(holder_string)

# # # Using lists - gives the same errors in judge, don't know why

first_string = input()
second_string = input()

first_string_list = list(first_string)
second_string_list = list(second_string)

word_length = len(second_string)

new_word = first_string_list

for i in range(word_length-1):
    if first_string_list[i] != second_string_list[i]:
        new_word[i] = second_string_list[i]
        print(''.join(new_word))

