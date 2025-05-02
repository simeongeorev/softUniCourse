from functools import reduce

employees_scores = list(map(int, input().split()))
multiplier = int(input())

multiplied_results = [score * multiplier for score in employees_scores]

average_score = reduce(lambda a, b: a + b, multiplied_results) / len(multiplied_results)

count_happy_ppl = [n for n in multiplied_results if n >= average_score]

if len(count_happy_ppl) >= int(len(employees_scores) / 2):
    print(f"Score: {len(count_happy_ppl)}/{len(employees_scores)}. Employees are happy!")
else:
    print(f"Score: {len(count_happy_ppl)}/{len(employees_scores)}. Employees are not happy!")

