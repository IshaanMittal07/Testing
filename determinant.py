def determinant(matrix):
    # Ensure matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")

    # Base case 1x1
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case 2x2
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive case for larger matrices
    det = 0
    for col in range(len(matrix)):
        # Build the submatrix
        submatrix = [
            [matrix[i][j] for j in range(len(matrix)) if j != col]
            for i in range(1, len(matrix))
        ]

        # Apply cofactor expansion along the first row
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)

    return det


# Example usage:
A = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

print("Determinant:", determinant(A))
