import math


def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result
    elif operator == "*":
        return math.prod(args)
    elif operator == "/":
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result


print(operate("/", 3, 4, 5, 3, 1))
