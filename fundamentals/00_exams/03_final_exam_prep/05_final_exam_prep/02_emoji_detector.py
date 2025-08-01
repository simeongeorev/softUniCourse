import re
from functools import reduce
from operator import mul

text = input()

num_pattern = r"\d"
num_matches = re.findall(num_pattern, text)
coolness_threshold = reduce(mul, list(map(int, num_matches)))

emoji_pattern = r"(?P<sym>[:]{2}|[*]{2})[A-Z][a-z]{2,}(?P=sym)"
emoji_matches = re.finditer(emoji_pattern, text)

emoji_count = 0
cool_emojis_list = []

for emoji in emoji_matches:
    emoji_count += 1
    clean_emoji = emoji.group()[2:-2]
    emoji_score = 0
    for char in clean_emoji:
        emoji_score += ord(char)
    if emoji_score > coolness_threshold: cool_emojis_list.append(emoji.group())

print(f"Cool threshold: {coolness_threshold}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in cool_emojis_list:
    print(emoji)
