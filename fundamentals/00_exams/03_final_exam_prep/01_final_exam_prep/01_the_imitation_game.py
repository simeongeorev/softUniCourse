encrypted_mess = list(input())

while True:

    command_ = input()

    if command_ == "Decode":
        break

    elif command_.startswith("Move"):
        num_of_letters = int(command_.split("|")[1])

        moving_letters = encrypted_mess[:num_of_letters]
        del encrypted_mess[:num_of_letters]
        encrypted_mess += moving_letters

    elif command_.startswith("Insert"):
        command_list = command_.split("|")
        index = int(command_list[1])
        value = command_list[2]

        moving_letters = encrypted_mess[index:]
        del encrypted_mess[index:]
        encrypted_mess += value
        encrypted_mess += moving_letters

    elif command_.startswith("ChangeAll"):
        command_list = command_.split("|")
        substring = command_list[1]
        replacement = command_list[2]

        encrypted_mess = [replacement if char == substring else char for char in encrypted_mess]

message_str = "".join(encrypted_mess)
print(f"The decrypted message is: {message_str}")