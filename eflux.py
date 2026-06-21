# Electric Flux Calculator using Gauss's Law

EPSILON_0 = 8.854e-12  # Permittivity of free space (C²/N·m²)

def calculate_flux(charge):
    return charge / EPSILON_0

def main():
    print("Electric Flux Calculator")
    print("------------------------")

    charge = float(input("Enter enclosed charge (C): "))

    flux = calculate_flux(charge)

    print(f"\nElectric Flux = {flux:.6e} N·m²/C")

if __name__ == "__main__":
    main()
