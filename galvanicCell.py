def parse_line_notation(line_notation):
    try:
        anode_half, cathode_half = line_notation.split("||")
    except ValueError:
        return "Invalid input: use '||' to separate anode and cathode."

    def parse_half_cell(half):
        components = [comp.strip() for comp in half.split("|")]
        return components

    anode_components = parse_half_cell(anode_half)
    cathode_components = parse_half_cell(cathode_half)

    return anode_components, cathode_components


def get_electrode_material(components):
    # Electrode is usually the first or last if it's a solid
    if components[0].endswith("(s)"):
        return components[0]
    elif components[-1].endswith("(s)"):
        return components[-1]
    else:
        return "Inert Electrode (e.g., Pt(s))"


def create_cell_diagram(line_notation):
    anode, cathode = parse_line_notation(line_notation)

    anode_electrode = get_electrode_material(anode)
    cathode_electrode = get_electrode_material(cathode)

    diagram = f"""
    +-----------------------+
    |     GALVANIC CELL     |
    +-----------------------+

    ANODE (oxidation):   {anode_electrode}
        {' --> '.join(anode)}

    Salt Bridge (||)

    CATHODE (reduction): {cathode_electrode}
        {' --> '.join(cathode)}

    Electrons flow: ANODE --> CATHODE
    """

    return diagram


# Example Usage
if __name__ == "__main__":
    line = input("Enter line diagram (e.g., Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s)): ")
    print(create_cell_diagram(line))
