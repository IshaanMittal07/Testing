from sympy import symbols
from sympy.logic.boolalg import simplify_logic
from sympy.parsing.sympy_parser import parse_expr

def simplify_boolean_expr(expr_str):
    try:
        # Parse the string into a sympy Boolean expression
        expr = parse_expr(expr_str, evaluate=False)
        
        # Simplify using boolean algebra
        simplified_expr = simplify_logic(expr, form='dnf')  # 'dnf' or 'cnf'
        
        return str(simplified_expr)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("=== Boolean Algebra Simplifier ===")
    print("Use symbols: & (AND), | (OR), ~ (NOT)")
    print("Example: ~(A & B) | (A & B)")
    
    expr_input = input("Enter Boolean Expression: ")
    result = simplify_boolean_expr(expr_input)
    
    print("\nSimplified Expression:")
    print(result)
