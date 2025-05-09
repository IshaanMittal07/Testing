import sympy as sp

def optimize_function(expr_str, variable_str='x'):
    # Define the variable and expression
    x = sp.symbols(variable_str)
    expr = sp.sympify(expr_str)
    
    # First and second derivatives
    first_derivative = sp.diff(expr, x)
    second_derivative = sp.diff(first_derivative, x)

    # Critical points: where first derivative is zero
    critical_points = sp.solve(first_derivative, x)

    results = []

    for point in critical_points:
        second_val = second_derivative.subs(x, point)
        nature = "minimum" if second_val > 0 else "maximum" if second_val < 0 else "inflection point"
        results.append({
            'point': point,
            'value': expr.subs(x, point),
            'type': nature
        })

    return results

# Example usage:
function_input = "x**3 - 6*x**2 + 9*x + 1"
results = optimize_function(function_input)

print(f"Function: {function_input}")
for res in results:
    print(f"\nAt x = {res['point']}:")
    print(f"  Type: {res['type']}")
    print(f"  Value: {res['value']}")
