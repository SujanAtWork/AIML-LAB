import unittest

from prim import prim


class TestPrim(unittest.TestCase):

    def setUp(self):

        self.graph = {
            "A": [("B", 2), ("C", 3)],
            "B": [("A", 2), ("C", 1), ("D", 1)],
            "C": [("A", 3), ("B", 1), ("D", 4), ("E", 5)],
            "D": [("B", 1), ("C", 4), ("E", 2)],
            "E": [("C", 5), ("D", 2)]
        }

    def test_mst_cost(self):

        mst, cost = prim(
            self.graph,
            "A"
        )

        self.assertEqual(cost, 6)

    def test_mst_edge_count(self):

        mst, cost = prim(
            self.graph,
            "A"
        )

        self.assertEqual(
            len(mst),
            len(self.graph) - 1
        )

    def test_invalid_start(self):

        with self.assertRaises(ValueError):
            prim(self.graph, "Z")

    def test_disconnected_graph(self):

        graph = {
            "A": [("B", 1)],
            "B": [("A", 1)],
            "C": []
        }

        with self.assertRaises(ValueError):
            prim(graph, "A")


if __name__ == "__main__":
    unittest.main()
