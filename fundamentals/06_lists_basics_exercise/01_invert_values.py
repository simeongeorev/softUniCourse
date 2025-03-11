# initialising list with elements separated by blank spaces
int_list = input().split()
for i in range(0, len(int_list)):
    int_list[i] = int(int_list[i])
    if int_list[i] > 0:
        int_list[i] = -abs(int_list[i])
    elif int_list[i] < 0:
        int_list[i] = abs(int_list[i])
print(int_list)
