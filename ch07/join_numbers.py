def join_numbers(rge: range) -> str:
    return ",".join([str(x) for x in rge])

print(join_numbers(range(15)))

def sum_hex(hex_strings: list) -> int:
    return sum(int(x, 16) for x in hex_strings)

print(sum_hex(["0x1", "0x10"]))
print(sum_hex(["0x1", "0x10", "0x15"]))
