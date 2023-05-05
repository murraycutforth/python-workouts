def get_sv(filepath):
    sv_words = []
    vowels = "aeiou"
    vowel_set = set(vowels)

    with open(filepath) as infile:
        for line in infile:
            word = line.strip()
            filtered_word = "".join(filter(lambda x: x in vowel_set, word))

            if filtered_word == vowels:
                sv_words.append(word)

    return sv_words

print(get_sv("words.txt"))
