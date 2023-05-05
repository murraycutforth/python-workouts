def reverse_lines():
    input_name = "reverse_me.txt"
    output_name = "reversed.txt"
    
    reversed_lines = []

    with open(input_name, "r") as infile:
        for line in infile:
            reversed_lines.append(line[-2:-len(line) - 1:-1] + "\n")

    with open(output_name, "w") as outfile:
        for line in reversed_lines:
            outfile.write(line)


reverse_lines()
