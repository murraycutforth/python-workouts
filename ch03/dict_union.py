from collections import defaultdict

def dict_union(list_of_dicts):
    result = defaultdict(list)
    for d in list_of_dicts:
        for k, v in d.items():
            result[k].append(v)

    result = dict(result)

    for k, v in result.items():
        if len(v) == 1:
            result[k] = v[0]

    return result


print(dict_union([{"a": 1, "b": 2}, {"a": 5, "c": 10}]))

