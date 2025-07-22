import re

text = input()

all_matches = []

while text:

    pattern = r"\d+"

    all_matches += re.findall(pattern, text)

    text = input()

print(" ".join(all_matches))