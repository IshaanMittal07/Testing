import numpy as np
import matplotlib.pyplot as plt

# Example: A + B -> products, rate = k * [A]^m * [B]^n

def rate_law(A, B, k, m, n):
    return k * (A**m) * (B**n)

def euler_method(A0, B0, k, m, n, dt, t_max):
    times = np.arange(0, t_max + dt, dt)
    A_conc = []
    B_conc = []

    A = A0
    B = B0

    for t in times:
        A_conc.append(A)
        B_conc.append(B)

        rate = rate_law(A, B, k, m, n)

        # Assume 1:1 stoichiometry: d[A]/dt = -rate, d[B]/dt = -rate
        A -= rate * dt
        B -= rate * dt

        # Prevent negative concentrations
        A = max(A, 0)
        B = max(B, 0)

    return times, A_conc, B_conc

# ==== USER INPUT ====
A0 = 1.0       # Initial [A] in mol/L
B0 = 1.0       # Initial [B] in mol/L
k = 0.5        # Rate constant in L/(mol*s)
m = 1          # Order of reaction with respect to A
n = 1          # Order of reaction with respect to B
dt = 0.01      # Time step (s)
t_max = 10     # Total time (s)

# ==== RUN SIMULATION ====
times, A_conc, B_conc = euler_method(A0, B0, k_
