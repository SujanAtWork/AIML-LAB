"""
Assignment No. 2
Title: Implement Greedy Search Algorithm

Application: Selection Sort

Selection Sort repeatedly selects the minimum element from the
unsorted portion of the array and places it at the correct position.

Greedy Choice:
    Select the smallest element from the remaining unsorted portion.

Time Complexity:
    Best Case    : O(n^2)
    Average Case : O(n^2)
    Worst Case   : O(n^2)

Space Complexity:
    O(1) auxiliary space
"""


def selection_sort(arr):
    """
    Sort a list using the Selection Sort algorithm.

    Parameters:
        arr (list): List of comparable elements.

    Returns:
        list: Sorted copy of the input list.
    """
    result = arr.copy()
    n = len(result)

    for i in range(n - 1):
        min_index = i

        # Greedy choice: find the smallest remaining element.
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        # Put the minimum element in its correct position.
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]

    return result


def main():
    """Demonstrate Selection Sort."""
    arr = [64, 25, 12, 22, 11]

    print("=" * 50)
    print("SELECTION SORT")
    print("=" * 50)

    print("Original Array:", arr)
    print("Sorted Array:  ", selection_sort(arr))


if __name__ == "__main__":
    main()
