letters = list(input())

def remove_vowels(chars):
    no_vowels_letters = [letter for letter in chars if not letter in ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']]
    return no_vowels_letters

print("".join(remove_vowels(letters)))