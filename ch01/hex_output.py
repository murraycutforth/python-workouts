def hex_output():
    n = input("Enter hex digits: ")

    result = 0
    for i, digit in enumerate(reversed(n)):
        result += int(digit, base=16) * 16**i

    print(result)


hex_output()
