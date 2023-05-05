import operator

def calc(prefix_str):
    all_args = prefix_str.split()
    op = all_args[0]
    args = [int(x) for x in all_args[1:]]

    op_table = {
            "+": operator.add,
    }

    result = op_table[op](args[0], args[1])
    for number in args[2:]:
        result = op_table[op](result, number)

    return result


print(calc("+ 3 4 5"))
print(calc("+ 3 4 "))

