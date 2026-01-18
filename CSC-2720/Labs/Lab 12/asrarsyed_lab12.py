# Course Section: CSC 2720-012

"""
Assignment: Solve Leetcode Problem 743: Network Delay Time
            https://leetcode.com/problems/network-delay-time/description/

Note: You should use Dijkstra’s algorithm to solve this problem.
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))  # Add each directed edge with its travel time

        # Initialize the minHeap and the shortest times dictionary
        minHeap = [(0, k)]
        # Initialize distances to infinity
        shortest_times = {i: float("inf") for i in range(1, n + 1)}
        shortest_times[k] = 0

        # Perform the Dijkstra's algorithm
        while minHeap:

            # Get the node with the smallest travel time
            current_time, node = heapq.heappop(minHeap)

            # If we've already found a shorter path to this node, skip it
            if current_time > shortest_times[node]:
                continue

            # Update the shortest paths to each neighbor
            for neighbor, travel_time in graph[node]:

                # Calculate time to reach the neighbor
                new_time = current_time + travel_time

                # If a shorter path is found, update it and push to the heap
                if new_time < shortest_times[neighbor]:
                    shortest_times[neighbor] = new_time
                    heapq.heappush(minHeap, (new_time, neighbor))

        # Determine the maximum time it takes to reach any node
        max_time = max(shortest_times.values())

        # If any node is unreachable (still has infinity time), return -1
        return max_time if max_time < float("inf") else -1
