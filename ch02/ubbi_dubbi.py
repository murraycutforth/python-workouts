def ubbi_dubbi(word: str) -> str:
    vowels = set("aeiou")
    result = []

    for char in word:
        if char in vowels:
            result.append("ub")
        result.append(char)

    return "".join(result)


print(ubbi_dubbi("octopus"))
print(ubbi_dubbi("elephant"))
