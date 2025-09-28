def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == "even":
            kwargs[k] = list(filter(lambda x: x % 2 == 0, v))
        else:
            kwargs[k] = list(filter(lambda x: x % 2 != 0, v))
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))