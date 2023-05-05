def get_sv(filepath):
    words = []

    vowel_set = set("aeiou")
    with open(filepath) as infile:
        for line in infile:
            word = line.strip()
            if set(word) > vowel_set:
                words.append(word)

    return words

print(get_sv("words.txt"))
