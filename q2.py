import numpy as np

A = np.array([[3, -2],
              [1, 0]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
for eigenvalue in eigenvalues:
    print(eigenvalue)

print("\nRight Eigenvectors:")
for i in range(len(eigenvectors)):
    print("Eigenvector", i+1, ":", eigenvectors[:, i])
