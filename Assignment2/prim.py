"""
Assignment No. 2
Title: Implement Greedy Search Algorithm

Application: Prim's Minimum Spanning Tree Algorithm

Prim's algorithm constructs a Minimum Spanning Tree (MST) of a
connected, weighted, undirected graph.

Greedy Choice:
    Select the minimum-weight edge that connects a visited vertex
    to an unvisited vertex.

Time Complexity:
    O(E log V) using a priority queue.

Space Complexity:
    O(V + E)
"""

import heapq


def prim(graph, start):
    """
    Find the Minimum Spanning Tree using Prim's algorithm.

    Parameters:
        graph (dict): Undirected adjacency-list graph.
        start: Starting vertex.

    Returns:
        tuple:
            mst: List of (u, v, weight)
            total_cost: Total weight of MST
    """

    if not graph:
        return [], 0

    if start not in graph:
        raise ValueError(
            f"Starting vertex '{start}' does not exist."
        )

    visited = {start}

    priority_queue = []

    # Add edges from starting vertex.
    for neighbor, weight in graph[start]:
        heapq.heappush(
            priority_queue,
            (weight, start, neighbor)
        )

    mst = []
    total_cost = 0

    while priority_queue:

        weight, u, v = heapq.heappop(priority_queue)

        # Ignore edges leading to already visited vertices.
        if v in visited:
            continue

        # Greedy choice:
        # Select the minimum edge connecting the MST to
        # an unvisited vertex.
        visited.add(v)

        mst.append((u, v, weight))
        total_cost += weight

        # Add new candidate edges.
        for neighbor, new_weight in graph[v]:

            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (new_weight, v, neighbor)
                )

    # If not all vertices were reached, the graph is disconnected.
    if len(visited) != len(graph):
        raise ValueError(
            "MST cannot be formed because the graph is disconnected."
        )

    return mst, total_cost


def main():
    """Demonstrate Prim's Algorithm."""

    graph = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 1), ("D", 1)],
        "C": [("A", 3), ("B", 1), ("D", 4), ("E", 5)],
        "D": [("B", 1), ("C", 4), ("E", 2)],
        "E": [("C", 5), ("D", 2)]
    }

    mst, total_cost = prim(graph, "A")

    print("=" * 50)
    print("PRIM'S MINIMUM SPANNING TREE")
    print("=" * 50)

    print("Edges in MST:")

    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total Cost =", total_cost)


if __name__ == "__main__":
    main()
