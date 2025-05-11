nums = list(map(int, input().split(", ")))

positives = [num for num in nums if num >= 0]
negatives = [num for num in nums if num < 0]
evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 != 0]

positives_str = ", ".join(list(map(str, positives)))
negatives_str = ", ".join(list(map(str, negatives)))
evens_str = ", ".join(list(map(str, evens)))
odds_str = ", ".join(list(map(str, odds)))

print(f"Positive: {positives_str}")
print(f"Negative: {negatives_str}")
print(f"Even: {evens_str}")
print(f"Odd: {odds_str}")