"""
Assignment No. 2
Title: Implement Greedy Search Algorithm

Application: Kruskal's Minimum Spanning Tree Algorithm

Kruskal's algorithm builds an MST by repeatedly selecting the
smallest-weight edge that does not create a cycle.

Greedy Choice:
    Select the smallest available edge that does not create a cycle.

Time Complexity:
    O(E log E)

Space Complexity:
    O(V)
"""


class DisjointSet:
    """
    Disjoint Set / Union-Find data structure.

    Uses:
        - Path compression
        - Union by rank
    """

    def __init__(self, vertices):
        """Initialize every vertex as its own set."""

        self.parent = {
            vertex: vertex
            for vertex in vertices
        }

        self.rank = {
            vertex: 0
            for vertex in vertices
        }

    def find(self, item):
        """
        Find the representative/root of a set.
        """

        if self.parent[item] != item:

            self.parent[item] = self.find(
                self.parent[item]
            )

        return self.parent[item]

    def union(self, x, y):
        """
        Merge the sets containing x and y.

        Returns:
            bool: True if union happened, False if they
                  were already in the same set.
        """

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank.
        if self.rank[root_x] < self.rank[root_y]:

            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:

            self.parent[root_y] = root_x

        else:

            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(vertices, edges):
    """
    Find the Minimum Spanning Tree using Kruskal's algorithm.

    Parameters:
        vertices (list): List of graph vertices.
        edges (list): List of (u, v, weight).

    Returns:
        tuple:
            mst: List of selected edges.
            total_cost: Total MST weight.
    """

    if not vertices:
        return [], 0

    vertex_set = set(vertices)

    # Validate edges.
    for u, v, weight in edges:

        if u not in vertex_set or v not in vertex_set:
            raise ValueError(
                f"Edge ({u}, {v}) contains an unknown vertex."
            )

        if weight < 0:
            raise ValueError(
                "Edge weights must not be negative."
            )

    # Sort edges by increasing weight.
    sorted_edges = sorted(
        edges,
        key=lambda edge: edge[2]
    )

    disjoint_set = DisjointSet(vertices)

    mst = []
    total_cost = 0

    for u, v, weight in sorted_edges:

        # Greedy choice:
        # Add the smallest edge only if it does not create a cycle.
        if disjoint_set.union(u, v):

            mst.append((u, v, weight))
            total_cost += weight

            # MST has V - 1 edges.
            if len(mst) == len(vertices) - 1:
                break

    # Check whether graph was connected.
    if len(mst) != len(vertices) - 1:
        raise ValueError(
            "MST cannot be formed because the graph is disconnected."
        )

    return mst, total_cost


def main():
    """Demonstrate Kruskal's Algorithm."""

    vertices = [
        "A",
        "B",
        "C",
        "D",
        "E"
    ]

    edges = [
        ("A", "B", 2),
        ("A", "C", 3),
        ("B", "C", 1),
        ("B", "D", 1),
        ("C", "D", 4),
        ("C", "E", 5),
        ("D", "E", 2)
    ]

    mst, total_cost = kruskal(
        vertices,
        edges
    )

    print("=" * 50)
    print("KRUSKAL'S MINIMUM SPANNING TREE")
    print("=" * 50)

    print("Edges in MST:")

    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total Cost =", total_cost)


if __name__ == "__main__":
    main()
