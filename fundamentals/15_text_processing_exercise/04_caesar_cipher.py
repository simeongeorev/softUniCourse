text = input()
encrypted_text = ""

for char in text:
    original_position = ord(char)
    new_position = original_position + 3
    new_char = chr(new_position)
    encrypted_text += new_char

print(encrypted_text)