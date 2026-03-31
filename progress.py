# Karp's 21 NP-Complete Problems (Karp 1972)
# Reference: Andrew Lucas, "Ising formulations of many NP problems", arXiv:1302.5843
#
# Lucas covers all 21 of Karp's problems plus several additional NP-hard problems.
# Some Karp problems are closely related (e.g. Clique and Vertex Cover), so we
# may be able to reuse code across multiple problems.
# Some Karp problems are easier to solve as NP-Hard variants, versus NP-complete
# In most cases, H = 0 is required to resolve YES for NP-complete problems,
# whereas for NP-hard problems we want to minimize H (has been found to be negative).

karp_21 = {
    # --- IMPLEMENTED ---
    "Clique": {
        "lucas": "§2.3",
        "status": "done",
        "file": "cliques.ipynb, largest_clique.ipynb",
    },
    "Vertex Cover": {
        "lucas": "§4.3",
        "status": "done",
        "file": "vertex_cover.ipynb, quantum_anneal_vc.ipynb",
    },
    "Partition": {
        "lucas": "§2.1",
        "status": "done",
        "file": "number_partitioning.ipynb",
    },
    "Max Cut": {
        "lucas": "§2.2 (native Ising)",
        "status": "done",
        "file": "maxcut.ipynb",
    },
    "Directed Hamiltonian Circuit": {
        "lucas": "§7.1",
        "status": "done",
        "file": "hamiltonian_cycle.ipynb",
    },
    "Undirected Hamiltonian Circuit": {
        "lucas": "§7.1",
        "status": "done",
        "file": "hamiltonian_cycle.ipynb, hamiltonian_path.ipynb",
    },
    "Set Packing": {
        "lucas": "§4.2 (= MIS on graphs)",
        "status": "done",
        "file": "set_packing.ipynb",
    },
    "SAT": {"lucas": "§4.4 (via 3-SAT → MIS)", "status": "done", "file": "sat3.ipynb"},
    "Exact Cover": {"lucas": "§4.1", "status": "done", "file": "exact_cover.ipynb"},
    "Graph Coloring": {
        "lucas": "§6.1",
        "status": "done",
        "file": "graph_colouring.ipynb",
    },
    "Clique Cover": {"lucas": "§6.2", "status": "done", "file": "clique_cover.ipynb"},
    "0-1 Integer Programming": {
        "lucas": "§3",
        "status": "in progress",
        "file": "integer_programming.ipynb",
    },
    "Knapsack": {"lucas": "§5.2", "status": "done", "file": "knapsack.ipynb"},
    "Job Sequencing": {
        "lucas": "§6.3",
        "status": "in progress",
        "file": "job_sequencing.ipynb",
    },
    # --- NOT YET IMPLEMENTED ---
    "Set Cover": {"lucas": "§5.1", "status": "todo"},
    "Feedback Vertex Set": {
        "lucas": "§8.3 (directed), §8.4 (undirected)",
        "status": "todo",
    },
    "Feedback Arc Set": {"lucas": "§8.5", "status": "todo"},
    "3D Matching": {"lucas": "§4.1 (special case of Exact Cover)", "status": "todo"},
    "Hitting Set": {"lucas": "§5.1 (dual of Set Cover)", "status": "todo"},
    "Steiner Tree": {"lucas": "§8.2", "status": "todo"},
}

# Additional problems from Lucas (not in Karp's 21)
lucas_extra = {
    "Graph Partitioning": {
        "lucas": "§2.2",
        "status": "done",
        "file": "graph_partitioning.ipynb",
    },
    "Travelling Salesman": {"lucas": "§7.2", "status": "done", "file": "tsp.ipynb"},
    "Minimal Maximal Matching": {"lucas": "§4.5", "status": "todo"},
    "Min Spanning Tree (degree-constrained)": {"lucas": "§8.1", "status": "todo"},
    "Graph Isomorphism": {"lucas": "§9", "status": "todo"},
}
