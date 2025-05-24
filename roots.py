from scipy.optimize import fsolve

def find_root_custom_function(func, guess):
    root = fsolve(func, guess)
    return root

# Example usage:
f = lambda x: x**3 - 2*x - 5
initial_guess = 2
root = find_root_custom_function(f, initial_guess)
print("A root of the function is approximately:", root[0])
