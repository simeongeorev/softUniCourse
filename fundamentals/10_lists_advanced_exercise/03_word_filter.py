text = input().split()
even_words = [word for word in text if len(word) % 2 == 0]
print("\n".join(even_words))
