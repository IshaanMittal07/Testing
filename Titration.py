import numpy as np
import matplotlib.pyplot as plt

def titration_curve(
    acid_conc=0.1,      # Molarity of acid
    acid_vol=50,        # Volume of acid in mL
    base_conc=0.1,      # Molarity of base
    points=1000         # Number of points for the curve
):
    # Generate base volumes (0 to 2x equivalence volume)
    V_eq = (acid_conc * acid_vol) / base_conc
    base_vols = np.linspace(0, 2 * V_eq, points)
    
    pH = []
    for Vb in base_vols:
        if Vb == 0:
            H_conc = acid_conc
        elif Vb < V_eq:
            H_mol = acid_conc * acid_vol / 1000
            OH_mol = base_conc * Vb / 1000
            H_conc = (H_mol - OH_mol) / ((acid_vol + Vb) / 1000)
        elif Vb == V_eq:
            H_conc = 1e-7  # neutral
        else:
            OH_mol = base_conc * Vb / 1000
            H_mol = acid_conc * acid_vol / 1000
            excess_OH = (OH_mol - H_mol) / ((acid_vol + Vb) / 1000)
            H_conc = 1e-14 / excess_OH

        pH.append(-np.log10(H_conc))

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(base_vols, pH, label="Titration Curve", color='blue')
    plt.axvline(x=V_eq, color='red', linestyle='--', label='Equivalence Point')
    plt.title("Titration Curve (Strong Acid vs Strong Base)")
    plt.xlabel("Volume of Base Added (mL)")
    plt.ylabel("pH")
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the simulation
titration_curve()
