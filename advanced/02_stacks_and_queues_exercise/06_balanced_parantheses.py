from collections import deque

parentheses = input()
success_flag = True

if len(parentheses) % 2 != 0:
    success_flag = False
else:
    allowed_parenths = {"{": "}", "(": ")", "[": "]"}

    container = list()

    for char in parentheses:
        if char in allowed_parenths.keys():
            container.append(char)
        elif allowed_parenths[container[-1]] == char:
            container.pop()
        else:
            success_flag = False
            break

print("YES" if success_flag else "NO")
