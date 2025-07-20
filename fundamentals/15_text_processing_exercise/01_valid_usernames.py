usernames_list = input().split(', ')


def correct_length(text):
    if 3 <= len(text) <= 16:
        return True
    else:
        return False

def correct_symbols(text: str):
    new_text = text
    new_text = new_text.replace("-", "")
    new_text = new_text.replace("_", "")
    if new_text.isalnum():
        return True
    else:
        return False

usernames_list = [username for username in usernames_list if correct_length(username) and correct_symbols(username)]

for username in usernames_list:
    print(username)