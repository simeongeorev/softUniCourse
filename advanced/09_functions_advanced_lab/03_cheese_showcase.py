def sorting_cheeses(**kwargs):
    sorted_list = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    cheeses_str = ""
    for tup in sorted_list:
        cheeses_str += tup[0] + "\n"
        cheeses_str += "\n".join(str(x) for x in sorted(tup[1], reverse=True)) + "\n"
    return cheeses_str

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)