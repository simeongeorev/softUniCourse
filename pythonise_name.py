def pythonise(string):
    string_list = list(string)
    indexes_to_del = []

    for i in range(len(string_list)):
        if string_list[i] == " " or string_list[i] == "-":
            string_list[i] = "_"
        if string_list[i] == ".":
            indexes_to_del.append(i)

    for index in indexes_to_del:
        del string_list[index]

    return "".join(string_list).lower()

while True:
    command = input()
    if command == "end":
        break
    print(pythonise(command))