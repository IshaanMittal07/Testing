# Parallel Plate Capacitor Calculator

EPSILON_0 = 8.854e-12  # F/m

print("Parallel Plate Capacitor Calculator")

area = float(input("Enter plate area (m^2): "))
distance = float(input("Enter plate separation distance (m): "))
epsilon_r = float(input("Enter relative permittivity (εr): "))

capacitance = epsilon_r * EPSILON_0 * area / distance

print(f"\nCapacitance = {capacitance:.6e} F")
print(f"Capacitance = {capacitance * 1e12:.3f} pF")
print(f"Capacitance = {capacitance * 1e9:.3f} nF")
print(f"Capacitance = {capacitance * 1e6:.3f} μF")
