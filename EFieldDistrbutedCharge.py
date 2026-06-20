import numpy as np

epsilon0 = 8.854187817e-12
k = 1 / (4 * np.pi * epsilon0)

def electric_field_line(observation_point, charge_points, dq):
    """
    Computes E-field from a discretized line charge.

    observation_point: [x,y,z]
    charge_points: Nx3 array of charge element locations
    dq: charge on each element (C)

    Returns: [Ex, Ey, Ez]
    """
    E = np.zeros(3)

    for r_prime in charge_points:
        R = observation_point - r_prime
        R_mag = np.linalg.norm(R)

        if R_mag < 1e-12:
            continue

        dE = k * dq * R / (R_mag**3)
        E += dE

    return E


# Example: Uniform line charge on x-axis
L = 1.0                     # meters
Q = 1e-6                    # total charge (C)
N = 1000                    # number of elements

x = np.linspace(-L/2, L/2, N)
charge_points = np.column_stack((x,
                                 np.zeros(N),
                                 np.zeros(N)))

dq = Q / N

P = np.array([0, 0.5, 0])   # observation point

E = electric_field_line(P, charge_points, dq)

print("Electric Field:")
print(f"Ex = {E[0]:.3e} N/C")
print(f"Ey = {E[1]:.3e} N/C")
print(f"Ez = {E[2]:.3e} N/C")
print(f"|E| = {np.linalg.norm(E):.3e} N/C")
