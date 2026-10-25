import numpy as np

# Linear equations:
# 2x + 3y = 13
# 4x + y = 11

A = np.array([
    [2, 3],
    [4, 1]
], dtype=float)

B = np.array([13, 11], dtype=float)

# Solve linear equations
solution = np.linalg.solve(A, B)

# Matrix properties
determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Solution [x, y]:", solution)
print("Determinant:", determinant)
print("Inverse:\n", inverse)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)