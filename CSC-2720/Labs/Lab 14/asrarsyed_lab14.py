# Course Section: CSC 2720-012

"""
Assignment: Implement the counting sort algorithm in Python, assuming the range of input numbers is [MIN,MAX].
            Consider optimizing the extra space usage by using the range of the input.
"""

from typing import List


def countingSort(array: List[int]) -> List[int]:
    # Get the maximum and minimum values in the array
    min_val: int = min(array)
    max_val: int = max(array)

    # Creating the count array for the range [min_val, max_val]
    range_size: int = max_val - min_val + 1
    count: List[int] = [0] * range_size

    # Count the occurrences of each element in the array
    for num in array:
        count[num - min_val] += 1

    # Reconstructs the sorted array using range()
    sorted_array: List[int] = []
    for value in range(min_val, max_val + 1):
        sorted_array.extend([value] * count[value - min_val])

    return sorted_array


# Example usage:
if __name__ == "__main__":
    test_array = [4, 2, 2, 8, 3, 3, 1, 4, 0]
    sorted_array = countingSort(test_array)
    print("Sorted array:", sorted_array)
