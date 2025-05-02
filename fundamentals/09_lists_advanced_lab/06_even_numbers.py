nums = list(map(int, input().split(", ")))
found_indexes = map(lambda index: index if nums[index] % 2 == 0 else "no",
                    range(len(nums)))
filtered_indexes = list(filter(lambda even: even != "no", found_indexes))
print(filtered_indexes)