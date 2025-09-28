def age_assignment(*args, **kwargs):
    for name in args:
        starting_letter = name[0]
        kwargs[name] = kwargs.pop(starting_letter)

    kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))
    result = ""

    for name, age in kwargs.items():
        result += f"{name} is {age} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))