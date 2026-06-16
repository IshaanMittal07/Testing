def multiplexer(inputs, select):
    """
    inputs: list of input values (e.g. [0,1,0,1])
    select: integer representing the selected input
    """
    if select < 0 or select >= len(inputs):
        raise ValueError("Invalid select value")

    return inputs[select]


# Main program
num_inputs = int(input("Enter number of inputs (must be a power of 2): "))

inputs = []
for i in range(num_inputs):
    value = int(input(f"Enter value for I{i} (0 or 1): "))
    inputs.append(value)

select = int(input(f"Enter select value (0 to {num_inputs-1}): "))

output = multiplexer(inputs, select)

print("\nMUX Configuration:")
for i, value in enumerate(inputs):
    print(f"I{i} = {value}")

print(f"Selected Input: I{select}")
print(f"Output Y = {output}")
