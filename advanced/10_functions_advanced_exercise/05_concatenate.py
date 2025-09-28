def concatenate(*args, **kwargs):
    concat_str = ""
    for s in args:
        concat_str += s

    for k, v in kwargs.items():
        if k in concat_str:
            concat_str = concat_str.replace(k,v)

    return concat_str

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))