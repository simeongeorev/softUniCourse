import os


def print_error():
    print("An error occurred")


while (command := input()) != "End":
    command = command.split("-")
    task = command[0]
    file_name = command[1]

    if task == "Create":
        file = open(file_name, "w")
        file.close()

    elif task == "Add":
        with open(file_name, "a") as file:
            file.write(command[2]+"\n")

    elif task == "Replace":
        old_string, new_string = command[2], command[3]

        if not os.path.exists(file_name):
            print_error()
            continue

        # open to read the file
        with open(file_name, "r") as file:
            file_content = file.read()

        edited_content = file_content.replace(old_string, new_string)

        # open to overwrite with the edited content
        with open(file_name, "w") as file:
            file.write(edited_content)

    elif task == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print_error()
            continue