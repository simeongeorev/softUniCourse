# 🧵 Python Text Transformation Toolkit

# Step 1: Display a menu to the user
print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")


# 1. Reverse Text
def reverse_text(original_text: str):
    return original_text[::-1]


# 2. Convert to Uppercase
def convert_to_uppercase(original_text: str) -> str:
    return original_text.upper()


# 3. Convert to Lowercase
def convert_to_lowercase(original_text: str) -> str:
    return original_text.lower()


# 4. Title Case
def convert_to_title_case(original_text: str) -> str:
    return original_text.title()


# 5. Count Vowels
def count_vowels(original_text: str) -> int:
    vowels_count = 0
    for char in original_text:
        if char in ["a", "e", "i", "o", "u"]:
            vowels_count += 1
    return vowels_count


# 6. Remove All Spaces
def remove_spaces(original_text: str) -> str:
    return original_text.replace(" ", "")


# 7. Replace Vowels with '*'
def replace_vowels_with_asterisks(original_text: str) -> str:
    str_list = [char if char not in ["a", "e", "i", "o", "u"] else "*" for char in original_text]
    return "".join(str_list)


# 8. Check if Palindrome
def is_palindrome(original_text: str) -> bool:
    original_text = convert_to_lowercase(original_text)
    original_text = remove_spaces(original_text)
    return True if original_text == reverse_text(original_text) else False


# 9. Word Frequency Counter
# TODO to make it prettier - replace with regex for all special symbols
def unique_word_counts(original_text: str) -> list:
    original_text = original_text.replace(".", "")
    original_text = original_text.replace(",", "")
    original_text = original_text.replace("!", "")
    original_text = original_text.replace("?", "")
    original_text = convert_to_lowercase(original_text)
    words_list = original_text.split()
    words_dict = {}
    words_set = set(words_list)
    for unique_word in words_set:
        word_count = words_list.count(unique_word)
        words_dict.update({unique_word: word_count})
    words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return words_dict

while True:

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get the input string
    text = input("Enter the text: ")

    # Step 4: Apply the selected transformation
    if choice == 1:
        # Reverse the text using slicing or a loop
        print("The reversed text is:", reverse_text(text))

    elif choice == 2:
        # Convert the text to uppercase using string methods
        print("The converted text to uppercase is:", convert_to_uppercase(text))

    elif choice == 3:
        # Convert the text to lowercase using string methods
        print("The converted text to lowercase is:", convert_to_lowercase(text))

    elif choice == 4:
        # Convert the text to title case (capitalize each word)
        print("The converted text to title case is:", convert_to_title_case(text))

    elif choice == 5:
        # Count how many vowels are in the text (a, e, i, o, u)
        print(f"The text contains {count_vowels(text)} vowels.")

    elif choice == 6:
        # Remove all spaces from the string using replace() or join()
        print(f"The text without spaces is:", remove_spaces(text))

    elif choice == 7:
        # Replace all vowels with "*" using a loop or comprehension
        print(f"The text with asterisks, instead of spaces is:", replace_vowels_with_asterisks(text))

    elif choice == 8:
        # Check if the text is a palindrome (ignoring case and spaces)
        if is_palindrome(text):
            print("The text is a palindrome.")
        else:
            print("The text is not a palindrome.")

    elif choice == 9:
        # Count the frequency of each word and display the result
        print("The count of each word in the text is: ")
        for item in unique_word_counts(text):
            print(f"{item[0]} - {item[1]}")

    else:
        print("❌ Invalid choice! Please restart the program.")

    print("Do you want to continue with the program? (y/n)")
    end_command = input()

    if end_command != "y":
        break

    print("Do you want to continue using the same text? (y/n)")
    use_same_text_command = input()
    use_same_text_flag = True

    # TODO try using the same text 
    if use_same_text_command != "y":
        break


