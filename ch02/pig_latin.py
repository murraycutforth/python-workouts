def pig_latin():
    word = input("Enter lower case word for translation: ")

    vowels = {"a", "e", "i", "o", "u"}

    if word[0] in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


result = pig_latin()
print(result)
