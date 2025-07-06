company_users = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, user_id = command.split(" -> ")

    if company_name not in company_users.keys():
        company_users[company_name] = []
    company_users[company_name] += [user_id]

for company_name, employee_ids in company_users.items():
    filtered_ids = [id_ for i, id_ in enumerate(employee_ids) if id_ not in employee_ids[:i]]
    print(company_name)
    for id_ in filtered_ids:
        print(f"-- {id_}")
