def flatten(list_of_lists):
    return [x for inner_list in list_of_lists for x in inner_list]

print(flatten([[1, 2], [3, 4]]))

def flatten_odd(list_of_lists):
    return [int(x) for inner_list in list_of_lists for x in inner_list if str(x).isdigit() and int(x) % 2 == 1]

print(flatten_odd([[1, 2], [3, 4]]))
print(flatten_odd([[1, 2], [3, 4], ["a", "6", "7"]]))
