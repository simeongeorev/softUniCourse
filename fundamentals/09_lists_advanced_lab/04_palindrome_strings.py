words = input().split()
palindrome = input()

palindrome_words = [word for word in words if word[::-1] == word]
times_found = palindrome_words.count(palindrome)

print(palindrome_words)
print(f"Found palindrome {times_found} times")