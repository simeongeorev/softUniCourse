lang_dict = {}
lang_submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    command_list = command.split("-")

    if command_list[1] == "banned":
        username = command_list[0]
        for languages in lang_dict.values():
            if username in languages.keys():
                languages.pop(username)
    else:
        username, language, points = command_list
        points = int(points)
        if language not in lang_dict.keys():
            lang_dict[language] = {}
        if username not in lang_dict[language].keys():
            lang_dict[language][username] = points
        else:
            if points > lang_dict[language][username]:
                lang_dict[language][username] = points

        if language not in lang_submissions.keys():
            lang_submissions[language] = 0
        lang_submissions[language] += 1

print("Results:")
for student_info in lang_dict.values():
    for student, points in student_info.items():
        print(f"{student} | {points}")
print("Submissions:")
for lang, subs in lang_submissions.items():
    print(f"{lang} - {subs}")


