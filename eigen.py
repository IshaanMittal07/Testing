import numpy as np

def get_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    print("Enter the matrix row by row (space-separated):")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            raise ValueError("Each row must have exactly n values.")
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Eigenvalue & Eigenvector Calculator")
    print("----------------------------------")
    A = get_matrix()

    # Compute eigenvalues & eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors (columns correspond to eigenvalues):")
    print(eigenvectors)

if __name__ == "__main__":
    main()
