import numpy as np
import matplotlib.pyplot as plt

def slope_field(f, x_range, y_range, density=20):
    x = np.linspace(x_range[0], x_range[1], density)
    y = np.linspace(y_range[0], y_range[1], density)
    X, Y = np.meshgrid(x, y)

    # Calculate slopes at each grid point
    U = 1  # All arrows move 1 unit in x
    V = f(X, Y)

    # Normalize arrows
    N = np.sqrt(U**2 + V**2)
    U2 = U / N
    V2 = V / N

    plt.figure(figsize=(8, 6))
    plt.title("Slope Field")
    plt.quiver(X, Y, U2, V2, angles="xy")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def main():
    print("Enter a function f(x, y) for dy/dx:")
    user_input = input("f(x, y) = ")

    # Safely convert the input into a function
    def f(x, y):
        return eval(user_input)

    # Define plot ranges
    x_range = (-5, 5)
    y_range = (-5, 5)

    slope_field(f, x_range, y_range)

if __name__ == "__main__":
    main()
