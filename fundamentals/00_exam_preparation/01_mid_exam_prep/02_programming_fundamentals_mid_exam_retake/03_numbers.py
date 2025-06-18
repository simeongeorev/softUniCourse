int_array = list(map(int, input().split()))

median_number = sum(int_array) / len(int_array)

int_array_sorted = sorted(int_array, reverse=True)

top_five_list = [number for number in int_array_sorted if number > median_number]

if len(top_five_list) == 0:
    print('No')
else:
    if len(top_five_list) > 5:
        top_five_list = top_five_list[:5]
    print(' '.join(list(map(str, top_five_list))))
