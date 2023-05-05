PEOPLE = [{"first": "ruven", "last": "lerner", "email": ""},{"first": "donald", "last": "trump", "email": ""},{"first": "vladimir", "last": "putin", "email": ""}]


def alphabetise_names():
    return sorted(PEOPLE, key=lambda x: (x["first"], x["last"]))


print(alphabetise_names())
