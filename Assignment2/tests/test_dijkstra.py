import unittest

from dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):

    def setUp(self):

        self.graph = {
            "A": [("B", 4), ("C", 2)],
            "B": [("A", 4), ("C", 1), ("D", 5)],
            "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
            "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
            "E": [("C", 10), ("D", 2), ("F", 3)],
            "F": [("D", 6), ("E", 3)]
        }

    def test_shortest_distances(self):

        distances = dijkstra(
            self.graph,
            "A"
        )

        expected = {
            "A": 0,
            "B": 3,
            "C": 2,
            "D": 8,
            "E": 10,
            "F": 13
        }

        self.assertEqual(distances, expected)

    def test_source_distance(self):

        distances = dijkstra(
            self.graph,
            "A"
        )

        self.assertEqual(distances["A"], 0)

    def test_invalid_source(self):

        with self.assertRaises(ValueError):
            dijkstra(self.graph, "Z")

    def test_negative_edge(self):

        graph = {
            "A": [("B", -1)],
            "B": [("A", -1)]
        }

        with self.assertRaises(ValueError):
            dijkstra(graph, "A")


if __name__ == "__main__":
    unittest.main()
