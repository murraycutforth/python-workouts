def flip_dict(d):
    return {v:k for k,v in d.items()}

c = {"a":1, "b":2, "c":3}
print(flip_dict(c))
