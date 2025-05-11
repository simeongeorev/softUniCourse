current_version = int("".join(input().split(".")))

current_version += 1

current_version_list = list(str(current_version))
print(".".join(current_version_list))


# if 9 in current_version[1:]:
#     for i in range(len(current_version) - 1, 0, -1):
#         if current_version[i] >= 9:
#             current_version[i] = 0
#             current_version[i - 1] += 1
# else:
#     current_version[-1] += 1
#
# print(".".join(list(map(str, current_version))))
