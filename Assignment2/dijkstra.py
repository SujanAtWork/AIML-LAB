"""
Assignment No. 2
Title: Implement Greedy Search Algorithm

Application: Single-Source Shortest Path

Algorithm: Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a source vertex
to every other vertex in a weighted graph with non-negative
edge weights.

Greedy Choice:
    Select the unvisited vertex with the smallest tentative distance.

Time Complexity:
    O((V + E) log V) using a priority queue.

Space Complexity:
    O(V + E)
"""

import heapq


def validate_graph(graph):
    """
    Validate that the graph contains no negative edge weights.
    """
    for vertex, neighbors in graph.items():

        for neighbor, weight in neighbors:

            if weight < 0:
                raise ValueError(
                    "Dijkstra's algorithm cannot be used with "
                    "negative edge weights."
                )

            if neighbor not in graph:
                raise ValueError(
                    f"Vertex '{neighbor}' is referenced but "
                    f"is not present in the graph."
                )


def dijkstra(graph, start):
    """
    Find shortest distances from start to all vertices.

    Parameters:
        graph (dict): Adjacency-list representation.
        start: Source vertex.

    Returns:
        dict: Shortest distance to each vertex.
    """

    if start not in graph:
        raise ValueError(
            f"Source vertex '{start}' does not exist in the graph."
        )

    validate_graph(graph)

    distances = {
        vertex: float("inf")
        for vertex in graph
    }

    distances[start] = 0

    # Priority queue contains:
    # (distance, vertex)
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_vertex = heapq.heappop(
            priority_queue
        )

        # Ignore outdated queue entries.
        if current_distance > distances[current_vertex]:
            continue

        # Relax all adjacent edges.
        for neighbor, weight in graph[current_vertex]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances


def dijkstra_with_paths(graph, start):
    """
    Find shortest distances and actual shortest paths.

    Returns:
        tuple:
            distances
            previous
    """

    if start not in graph:
        raise ValueError(
            f"Source vertex '{start}' does not exist in the graph."
        )

    validate_graph(graph)

    distances = {
        vertex: float("inf")
        for vertex in graph
    }

    previous = {
        vertex: None
        for vertex in graph
    }

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_vertex = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def reconstruct_path(previous, start, destination):
    """
    Reconstruct a shortest path using the previous-vertex dictionary.
    """

    if destination not in previous:
        return []

    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path


def main():
    """Demonstrate Dijkstra's Algorithm."""

    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)]
    }

    source = "A"

    distances, previous = dijkstra_with_paths(
        graph,
        source
    )

    print("=" * 50)
    print("DIJKSTRA'S SHORTEST PATH")
    print("=" * 50)

    print("Source Vertex:", source)
    print()

    for vertex in graph:
        distance = distances[vertex]

        if distance == float("inf"):
            print(f"{source} -> {vertex} = INF")
        else:
            path = reconstruct_path(
                previous,
                source,
                vertex
            )

            print(
                f"{source} -> {vertex} = {distance}"
                f"   Path: {' -> '.join(path)}"
            )


if __name__ == "__main__":
    main()
