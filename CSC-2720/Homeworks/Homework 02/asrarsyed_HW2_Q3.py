# Course Section: CSC 2720-012

"""
Assignment: Write a class named ‘PercentileMonitor’ with the following methods:
    • add(self, num): Adds the new number to the appropriate heap. Also, this method is responsible for keeping ‘balance’ between the heaps.
      Balancing is needed to access the 25th and 75th percentile efficiently.
    • get_25th(self): returns the 25th percentile of the data. It should run in O(1) time.
    • get_75th(self): returns the 75th percentile of the data. It should run in O(1) time.
"""

import heapq
from typing import List, Optional


class PercentileMonitor:
    def __init__(self):
        # For 25th percentile:
        self.first_quarter_maxheap: List[int] = []  # stores bottom 25% (as negatives)
        self.above_25th_minheap: List[int] = []  # stores remaining 75%

        # For 75th percentile:
        self.below_75th_maxheap: List[int] = []  # stores bottom 75% (as negatives)
        self.last_quarter_minheap: List[int] = []  # stores top 25%

        self.size: int = 0

    # Calculates the target sizes for heaps based on current total size.
    def calculate_sizes(self) -> tuple[int, int]:
        if self.size == 0:
            return 0, 0

        target_25th = (self.size - 1) // 4 + 1
        target_75th = (3 * (self.size - 1)) // 4 + 1
        return target_25th, target_75th

    # Adds a number and maintains both 25th and 75th percentile structures.
    def add(self, num: int) -> None:
        self.size += 1

        # Add to 25th percentile structure
        if len(self.first_quarter_maxheap) == 0 or -self.first_quarter_maxheap[0] > num:
            heapq.heappush(self.first_quarter_maxheap, -num)
        else:
            heapq.heappush(self.above_25th_minheap, num)

        # Add to 75th percentile structure
        if len(self.last_quarter_minheap) == 0 or self.last_quarter_minheap[0] <= num:
            heapq.heappush(self.last_quarter_minheap, num)
        else:
            heapq.heappush(self.below_75th_maxheap, -num)

        self.balance()

    # Balances both structures to maintain proper percentile positions.
    def balance(self) -> None:
        # Calculate target sizes for the heaps
        target_25th, target_75th = self.calculate_sizes()

        # Balance the 25th percentile structure
        while len(self.first_quarter_maxheap) > target_25th:  # Move excess from bottom 25% to the above 25th heap
            val = -heapq.heappop(self.first_quarter_maxheap)
            heapq.heappush(self.above_25th_minheap, val)

        while len(self.first_quarter_maxheap) < target_25th and self.above_25th_minheap:  # Move elements back to maintain the target size
            val = heapq.heappop(self.above_25th_minheap)
            heapq.heappush(self.first_quarter_maxheap, -val)

        # Balance the 75th percentile structure
        while len(self.below_75th_maxheap) > target_75th - 1:  # Move excess from bottom 75% to the top 25% heap
            val = -heapq.heappop(self.below_75th_maxheap)
            heapq.heappush(self.last_quarter_minheap, val)

        while len(self.below_75th_maxheap) < target_75th - 1 and self.last_quarter_minheap:  # Move elements back to maintain the target size
            val = heapq.heappop(self.last_quarter_minheap)
            heapq.heappush(self.below_75th_maxheap, -val)

    # Returns the 25th percentile in O(1) time.
    def get_25th(self) -> Optional[float]:
        if not self.first_quarter_maxheap:
            return None
        return float(-self.first_quarter_maxheap[0])  # Returns the largest of the bottom 25%

    # Returns the 75th percentile in O(1) time.
    def get_75th(self) -> Optional[float]:
        if not self.last_quarter_minheap:
            return None
        return float(self.last_quarter_minheap[0])  # Returns the smallest of the top 25%


# Example usage and test
def test_example():
    data = [13, 24, 28, 32, 33, 39, 40, 45, 46, 55, 56, 57, 58, 59, 60, 67, 68, 71, 74, 75, 80, 83, 84, 89, 90]

    # Test our implementation
    pm = PercentileMonitor()
    for num in data:
        pm.add(num)

    print(f"Actual 25th percentile: {pm.get_25th()}")
    print(f"Actual 75th percentile: {pm.get_75th()}")


if __name__ == "__main__":
    test_example()
