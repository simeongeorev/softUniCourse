number_of_groups = int(input())

musala_group = 0
monblan_group = 0
kiliman_group = 0
k2_group = 0
everest_group = 0
number_of_people_total = 0

for i in range(0, number_of_groups):

    number_of_people_in_group = int(input())

    number_of_people_total += number_of_people_in_group

    if number_of_people_in_group < 6:
        musala_group += number_of_people_in_group

    elif number_of_people_in_group < 13:
        monblan_group += number_of_people_in_group

    elif number_of_people_in_group < 26:
        kiliman_group += number_of_people_in_group

    elif number_of_people_in_group < 41:
        k2_group += number_of_people_in_group

    elif number_of_people_in_group >= 41:
        everest_group += number_of_people_in_group

print(f"{musala_group / number_of_people_total * 100:.2f}%")
print(f"{monblan_group / number_of_people_total * 100:.2f}%")
print(f"{kiliman_group / number_of_people_total * 100:.2f}%")
print(f"{k2_group / number_of_people_total * 100:.2f}%")
print(f"{everest_group / number_of_people_total * 100:.2f}%")
