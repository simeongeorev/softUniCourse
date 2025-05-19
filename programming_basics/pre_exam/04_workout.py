import math

n_days = int(input())
kms_ran_first_day = float(input())
new_base_for_increase = kms_ran_first_day
total_kms = kms_ran_first_day

for _ in range(n_days):
    percents_increase = int(input())
    increased_kms = new_base_for_increase + ((percents_increase / 100) * new_base_for_increase)
    total_kms += increased_kms
    new_base_for_increase = increased_kms

if total_kms >= 1_000:
    print(f"You've done a great job running {math.ceil(total_kms - 1_000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1_000 - total_kms)} more kilometers")

