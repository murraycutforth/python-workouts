def dictdiff(d1, d2):
    result = {}
    for k in d1.keys() | d2.keys():
        v1 = d1.get(k)
        v2 = d2.get(k)
        if v1 != v2:
            result[k] = [v1, v2]
    return result

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 2, "c": 4}

print(dictdiff(d2, d2))
print(dictdiff(d1, d2))


def mergedicts(*args):
    result = {}
    for d in args:
        result.update(d)
    return result

print(mergedicts({"a": 1}, {"a": 2}, {"a": 3, "b": 1}))


def dictconstruct(*args):
    result = {}
    for k, v in zip(args[::2], args[1::2]):
        result[k] = v
    return result

print(dictconstruct("a", 1, "b", 2))

