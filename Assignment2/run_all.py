"""
Assignment No. 2
Title: Implement Greedy Search Algorithm

This program demonstrates all greedy algorithms implemented
for Assignment 2.
"""

from selection_sort import selection_sort
from job_scheduling import job_scheduling
from dijkstra import dijkstra_with_paths, reconstruct_path
from prim import prim
from kruskal import kruskal


def demonstrate_selection_sort():
    print("\n1. SELECTION SORT")
    print("-" * 40)

    arr = [64, 25, 12, 22, 11]

    print("Original Array:", arr)
    print("Sorted Array:  ", selection_sort(arr))


def demonstrate_job_scheduling():
    print("\n2. JOB SCHEDULING")
    print("-" * 40)

    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 19),
        ("J3", 2, 27),
        ("J4", 1, 25),
        ("J5", 3, 15)
    ]

    scheduled_jobs, total_profit = job_scheduling(jobs)

    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)


def demonstrate_dijkstra():
    print("\n3. DIJKSTRA'S SHORTEST PATH")
    print("-" * 40)

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

    print("Source:", source)

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
                f" | Path: {' -> '.join(path)}"
            )


def demonstrate_prim():
    print("\n4. PRIM'S MINIMUM SPANNING TREE")
    print("-" * 40)

    graph = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 1), ("D", 1)],
        "C": [("A", 3), ("B", 1), ("D", 4), ("E", 5)],
        "D": [("B", 1), ("C", 4), ("E", 2)],
        "E": [("C", 5), ("D", 2)]
    }

    mst, total_cost = prim(graph, "A")

    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total Cost =", total_cost)


def demonstrate_kruskal():
    print("\n5. KRUSKAL'S MINIMUM SPANNING TREE")
    print("-" * 40)

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

    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total Cost =", total_cost)


def main():
    print("=" * 60)
    print("ASSIGNMENT NO. 2 - GREEDY SEARCH ALGORITHMS")
    print("=" * 60)

    demonstrate_selection_sort()
    demonstrate_job_scheduling()
    demonstrate_dijkstra()
    demonstrate_prim()
    demonstrate_kruskal()

    print("\n" + "=" * 60)
    print("ALL ALGORITHMS EXECUTED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
