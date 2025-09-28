def sum_nums(*args):
    positive_sum = 0
    negative_sum = 0
    result_str = ""
    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num

    result_str += f"{negative_sum}\n"
    result_str += f"{positive_sum}\n"

    if abs(negative_sum) > positive_sum:
        result_str += "The negatives are stronger than the positives"
    else:
        result_str += "The positives are stronger than the negatives"
    return result_str


numbers = (map(int, input().split()))
print(sum_nums(*numbers))
