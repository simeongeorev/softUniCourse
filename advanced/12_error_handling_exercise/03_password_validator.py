from string import punctuation


class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


special_chars = ["@", "*", "&", "%"]

while (password := input()) != "Done":
    # validate password's length
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    # validate if the password has mixed symbols
    if password.isnumeric() or password.isalpha() or all(letter in punctuation for letter in password):
        raise PasswordTooCommonError(
            "Password must be a combination of digits, letters, and special characters")

    # validate if the password contains approved by the task special characters
    has_approved_specials = any(letter in special_chars for letter in password)
    if not has_approved_specials:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    # validate if the password contains empty spaces
    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    # print a valid password
    print("Password is valid")
