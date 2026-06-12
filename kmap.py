# 4-variable Karnaugh Map Generator

def generate_kmap(minterms):
    # Gray code ordering
    gray = [0, 1, 3, 2]

    # Create 4x4 K-map
    kmap = [[0 for _ in range(4)] for _ in range(4)]

    for m in minterms:
        row_bits = (m >> 2) & 0b11  # AB
        col_bits = m & 0b11         # CD

        row = gray.index(row_bits)
        col = gray.index(col_bits)

        kmap[row][col] = 1

    return kmap


def print_kmap(kmap):
    labels = ["00", "01", "11", "10"]

    print("      CD")
    print("      " + "  ".join(labels))
    print("AB  +----------------")

    for i, row in enumerate(kmap):
        print(labels[i], "|", "  ".join(str(x) for x in row))


# Example
minterms = [0, 1, 2, 5, 7, 8, 10, 13, 15]

kmap = generate_kmap(minterms)
print_kmap(kmap)
