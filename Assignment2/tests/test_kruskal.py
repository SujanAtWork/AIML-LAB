import unittest

from kruskal import kruskal


class TestKruskal(unittest.TestCase):

    def setUp(self):

        self.vertices = [
            "A",
            "B",
            "C",
            "D",
            "E"
        ]

        self.edges = [
            ("A", "B", 2),
            ("A", "C", 3),
            ("B", "C", 1),
            ("B", "D", 1),
            ("C", "D", 4),
            ("C", "E", 5),
            ("D", "E", 2)
        ]

    def test_mst_cost(self):

        mst, cost = kruskal(
            self.vertices,
            self.edges
        )

        self.assertEqual(cost, 6)

    def test_mst_edge_count(self):

        mst, cost = kruskal(
            self.vertices,
            self.edges
        )

        self.assertEqual(
            len(mst),
            len(self.vertices) - 1
        )

    def test_disconnected_graph(self):

        vertices = ["A", "B", "C"]

        edges = [
            ("A", "B", 1)
        ]

        with self.assertRaises(ValueError):
            kruskal(vertices, edges)


if __name__ == "__main__":
    unittest.main()
