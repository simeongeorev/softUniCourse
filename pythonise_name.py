def pythonise(string):
    string = string.lower()
    string = string.replace(" ", "_")
    string = string.replace("-", "_")
    string = string.replace(".", "")
    string = string.replace("'", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    return string


while True:
    command = input()
    if command == "end":
        break
    print(pythonise(command))
