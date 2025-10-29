from project.library import Library
from project.user import User


class Registration:

    def __init__(self):
        pass

    def add_user(self, user: User, library: Library) -> None | str:
        if user not in library.user_records:
            library.user_records.append(user)
            return None
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> None | str:
        if user in library.user_records:
            library.user_records.remove(user)
            return None
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        current_user = next((u for u in library.user_records
                             if u.user_id == user_id), None)

        if not current_user:
            return f"There is no user with id = {user_id}!"

        if current_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if current_user.username in library.rented_books.keys():
            # changing the key name in the rented_books dict
            library.rented_books[new_username] = library.rented_books.pop(current_user.username)

        current_user.username = new_username

        return f"Username successfully changed to: {new_username} for user id: {user_id}"





