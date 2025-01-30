open_tabs = int(input())
salary = int(input())

fine = 0
salary_left = 0

for i in range(0, open_tabs):
    tab_name = str(input())
    if tab_name == "Facebook":
        fine += 150
    elif tab_name == "Instagram":
        fine += 100
    elif tab_name == "Reddit":
        fine += 50

    salary_left = salary - fine

    if salary_left <= 0:
        print("You have lost your salary.")
        exit()

print(salary_left)

