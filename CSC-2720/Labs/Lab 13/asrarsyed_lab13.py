# Course Section: CSC 2720-012

"""
Assignment: Solve HackerRank – Trie - Contacts
            https://www.hackerrank.com/challenges/contacts/problem

Note: Use a Trie to solve this problem. The trie implementation must be based on a hash table (e.g. Python dictionary).
"""

#!/bin/python3

import os

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#


class TrieNode:
    def __init__(self):
        # Each node has a dictionary for child nodes and a count for prefix tracking
        self.children = {}
        self.count = 0  # Number of words sharing this prefix


class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def add(self, name: str) -> None:
        # Add a name to the Trie
        current = self.root
        for char in name:
            # If the character is not already a child, create a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the child node
            current = current.children[char]
            # Increment count for this prefix
            current.count += 1

    def find(self, prefix: str) -> int:
        # Find the count of names starting with the given prefix
        current = self.root
        for char in prefix:
            # If the character doesn't exist in the Trie, return 0
            if char not in current.children:
                return 0
            # Move to the next node
            current = current.children[char]
        # Return the count of names with this prefix
        return current.count


def contacts(queries):
    # Initialize the Trie and results list
    trie = Trie()
    results = []

    for operation, value in queries:
        if operation == "add":
            # Add the name to the Trie
            trie.add(value)
        elif operation == "find":
            # Find the number of names with the prefix and store the result
            results.append(trie.find(value))

    return results


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
