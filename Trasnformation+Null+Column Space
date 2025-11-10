import numpy as np
from sympy import Matrix

def main():
    print("=== Linear Transformation Analyzer ===")
    print("Enter the matrix representing your system (each row separated by commas).")
    print("Example: For [[1, 2], [3, 4]] enter: 1 2; 3 4")
    
    # Take input
    raw_input = input("\nMatrix A = ")
    # Parse into NumPy array
    try:
        rows = [list(map(float, r.split())) for r in raw_input.split(';')]
        A = np.array(rows)
    except Exception as e:
        print("❌ Invalid matrix format. Please enter rows separated by ';' and numbers separated by spaces.")
        return

    print("\nYour matrix A:")
    print(A)

    # Convert to sympy Matrix for symbolic computation
    M = Matrix(A)

    # Compute linear transformation info
    print("\n=== Linear Transformation Information ===")
    print(f"Input dimension (domain): {M.shape[1]}")
    print(f"Output dimension (codomain): {M.shape[0]}")

    # Compute rank
    rank = M.rank()
    print(f"Rank(A): {rank}")

    # Compute column space
    col_space = M.columnspace()
    print("\nColumn Space (basis vectors):")
    for v in col_space:
        print(np.array(v, dtype=float).flatten())

    # Compute null space
    null_space = M.nullspace()
    print("\nNull Space (basis vectors):")
    if len(null_space) == 0:
        print("[{0}] (Only the zero vector)")
    else:
        for v in null_space:
            print(np.array(v, dtype=float).flatten())

    # Show transformation form
    print("\n=== Transformation Form ===")
    print("T(x) = A * x, where")
    print("A =")
    print(M)

    print("\nSo for a vector x = (x1, x2, ..., xn)^T, the transformation T(x) is:")
    print("T(x) =")
    print(M * Matrix([f"x{i+1}" for i in range(M.shape[1])]))


if __name__ == "__main__":
    main()
