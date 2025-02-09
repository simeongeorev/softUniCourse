number_of_ns = int(input())
n_sum = 0
for i in range(number_of_ns):
    n = int(input())
    n_sum += n
print(f"{n_sum / number_of_ns:.2f}")