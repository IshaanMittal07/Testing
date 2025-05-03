import sympy as sp

def find_inflection_points(expr_str):
    x = sp.Symbol('x')
    
    # Parse the expression
    expr = sp.sympify(expr_str)
    
    # First and second derivatives
    first_derivative = sp.diff(expr, x)
    second_derivative = sp.diff(first_derivative, x)
    
    # Solve for where the second derivative is zero or undefined
    critical_points = sp.solveset(second_derivative, x, domain=sp.S.Reals)

    # Filter points where the second derivative changes sign
    inflection_points = []
    for point in critical_points:
        # Ensure it's a numerical point (skip symbolic ones like oo)
        if not point.is_real:
            continue

        # Use a small epsilon to test sign change
        epsilon = 1e-4
        left = second_derivative.subs(x, point - epsilon)
        right = second_derivative.subs(x, point + epsilon)

        if left * right < 0:
            y_value = expr.subs(x, point)
            inflection_points.append((float(point), float(y_value)))

    return inflection_points

# Example usage
if __name__ == "__main__":
    function = input("Enter a function in x (e.g., x**3 - 3*x + 1): ")
    points = find_inflection_points(function)

    if points:
        print("Inflection point(s):")
        for pt in points:
            print(f"x = {pt[0]:.5f}, y = {pt[1]:.5f}")
    else:
        print("No inflection points found.")
