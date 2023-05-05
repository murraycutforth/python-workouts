def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return  word[1:] + word[0] + "ay"

def pl_translation(filepath):
    with open(filepath) as infile:
        return " ".join(pig_latin(word) for word in infile.read().split())

print(pl_translation("test.txt"))
