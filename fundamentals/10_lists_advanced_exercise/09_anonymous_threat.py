input_list = input().split()

while True:
    command = input()
    if command == "3:1":
        for word in input_list:
            print(word, end=" ")
        break

    command = command.split()
    if "merge" in command:
        new_list = []
        start_index, end_index = int(command[1]), int(command[2])
        if start_index not in range(len(input_list)):
            start_index = 0
        if end_index not in range(len(input_list)):
            end_index = len(input_list) - 1
        merged_string = "".join(input_list[start_index:end_index + 1])
        input_list[start_index] = merged_string
        input_list = input_list[:start_index + 1] + input_list[end_index + 1:]

    elif "divide" in command:
        new_list = []
        index, partitions = int(command[1]), int(command[2])
        word_to_separate = input_list[index]
        length_of_word = len(word_to_separate)
        separated_word_list = []

        if length_of_word % partitions == 0:
            equal_chars_count = int(length_of_word / partitions)
            separated_word_list.append(word_to_separate[:equal_chars_count])

            for i in range(equal_chars_count,
                           length_of_word - equal_chars_count + 1,
                           equal_chars_count):
                separated_word_list.append(word_to_separate[i:i + equal_chars_count])

        else:
            equal_chars_count = int(length_of_word // partitions)
            chars_left_count = length_of_word % partitions
            separated_word_list.append(word_to_separate[0:equal_chars_count])

            for i in range(equal_chars_count,
                           length_of_word - equal_chars_count - chars_left_count + 1,
                           equal_chars_count):
                separated_word_list.append(word_to_separate[i:i + equal_chars_count])
            input_list[index][-1].join(input_list[index][-1][-chars_left_count:])

        for i in range(len(input_list)):
            if i == index:
                for word in separated_word_list:
                    new_list.append(word)
            else:
                new_list.append(input_list[i])

        input_list = new_list
