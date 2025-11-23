def type_check(type_input):
    def decorator(func):
        def wrapper(*args):
            if any(type(x) != type_input for x in args):
                return "Bad Type"
            return func(*args)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
