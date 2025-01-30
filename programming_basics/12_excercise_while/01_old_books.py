searched_book = input()
books_checked = 0
NO_MORE_BOOKS = "No More Books"

while True:
    nth_book = input()

    if nth_book == searched_book:
        print(f"You checked {books_checked} books and found it.")
        break

    elif nth_book != searched_book and nth_book != NO_MORE_BOOKS:
        books_checked += 1

    elif nth_book == NO_MORE_BOOKS:
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break
