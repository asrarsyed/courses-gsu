# Course Section: CSC 2720-012

"""
Assignment: Write a Python function named extractCycle(graph, start).

Input:      An adjacency list representing a directed graph and a start node.
Output:     If the ‘start’ node is part of a cycle, return the cycle as a list of nodes.
            Otherwise, return an empty list.

For example, when the method is called with the following graph with start=0, it should return [0, 1, 2, 4, 0]
"""

# Adjacency list representing the graph
adj = [[1, 3], [2], [4], [], [0, 3], [2]]


def extract_cycle(adj_list, start):
    visited = set()  # Track all visited nodes
    cur_path = []  # Current path to detect cycles
    path_set = set()  # Set version of the path

    def dfs(node):
        if node in path_set:  # Cycle found
            cycle_start_index = cur_path.index(node)
            return cur_path[cycle_start_index:] + [node]

        if node in visited:  # Node already processed and no cycle found through it
            return []

        visited.add(node)
        cur_path.append(node)
        path_set.add(node)

        for neighbor in adj_list[node]:
            result = dfs(neighbor)
            if result:  # If a cycle is found, return it
                return result

        # Backtrack
        cur_path.pop()
        path_set.remove(node)

        return []

    return dfs(start)


# Testing the function
adj = [[1, 3], [2], [4], [], [0, 3], [2]]
print(extract_cycle(adj, 0))  # Should print [0, 1, 2, 4, 0]
print(extract_cycle(adj, 1))  # Should print [1, 2, 4, 0, 1]
print(extract_cycle(adj, 3))  # Should print []
