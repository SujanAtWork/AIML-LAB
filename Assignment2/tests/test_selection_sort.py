import unittest

from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):

    def test_normal_list(self):
        self.assertEqual(
            selection_sort([64, 25, 12, 22, 11]),
            [11, 12, 22, 25, 64]
        )

    def test_empty_list(self):
        self.assertEqual(
            selection_sort([]),
            []
        )

    def test_single_element(self):
        self.assertEqual(
            selection_sort([5]),
            [5]
        )

    def test_duplicates(self):
        self.assertEqual(
            selection_sort([3, 1, 2, 1, 3]),
            [1, 1, 2, 3, 3]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            selection_sort([3, -1, 0, -5, 2]),
            [-5, -1, 0, 2, 3]
        )


if __name__ == "__main__":
    unittest.main()
    