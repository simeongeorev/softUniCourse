
def pass_length_check(password: str):
    if 5 < len(password) < 11:
        return True
    else:
        return False

def pass_chars_check(password: str):
    if password.isalnum():
        return True
    else:
        return False

def pass_digits_check(password: str):
    counter = 0
    for char in password:
        if char.isnumeric():
            counter+=1

    if counter >= 2:
        return True
    else:
        return False

def password_validate(password: str):
    if pass_length_check(password) and pass_chars_check(password) and pass_digits_check(password):
        print("Password is valid")
        return
    if not pass_length_check(password):
        print("Password must be between 6 and 10 characters")
    if not pass_chars_check(password):
        print("Password must consist only of letters and digits")
    if not pass_digits_check(password):
        print("Password must have at least 2 digits")

password_validate(input())
