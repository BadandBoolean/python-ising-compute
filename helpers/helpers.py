# helpers.py
# helpers for notebook functions
import numba
import numpy as np


# adjacency matrix of size NxN depicting undirected graph G = (V, E)
# 0 represents no connection, 1 represents a connection.
# diagonal is all zereos.
@numba.njit
def generate_adjacency_matrix_undirected(N, p):
    adjacency_matrix = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(i + 1, N):
            if np.random.rand() < p and i != j:
                # Only add an edge if i and j are not the same node
                # and the random condition is met
                adjacency_matrix[i, j] = 1
                adjacency_matrix[j, i] = 1
    return adjacency_matrix


def init_random_spins(N, num_dimensions=2):
    # Initialize a random n-dimensional spin configuration for N spins
    # e.g if num_dimensions=2, the matrix is NxN.
    # if num_dimensions=3, the matrix is NxNxN.
    # if num_dimensions=1, the matrix is Nx1.
    if num_dimensions == 2:
        matrix = np.random.randint(0, 2, size=(N, N))
        return matrix
    elif num_dimensions == 1:
        matrix = np.random.randint(0, 2, size=(N, 1))
        return matrix


# debugging
if __name__ == "__main__":
    N = 5
    p = 0.3
    adjacency_matrix = generate_adjacency_matrix_undirected(N, p)
    print("Adjacency Matrix:")
    print(adjacency_matrix)

    num_dimensions = 2
    spins = init_random_spins(N, num_dimensions)
    print("\nRandom Spin Configuration:")
    print(spins)

    num_dimensions = 1
    spins = init_random_spins(N, num_dimensions)
    print("\nRandom Spin Configuration (1D):")
    print(spins)
    spins_flat = spins.flatten()
    print("\nRandom Spin Configuration (flattened):")
    print(spins_flat)
