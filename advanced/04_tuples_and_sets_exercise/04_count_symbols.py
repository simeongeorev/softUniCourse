text = tuple(input())
char_counts = dict()
for char in text:
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1
sorted_char_counts = dict(sorted(char_counts.items()))
for char, count in sorted_char_counts.items():
    print(f"{char}: {count} time/s")