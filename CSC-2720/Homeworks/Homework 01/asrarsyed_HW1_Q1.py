# Course Section: CSC 2720-012

"""
Assignment: An array of elements is given.
            The task is to find the next greater for each element in the array.
            If there is no greater element to the right of the element, then return -1.

Limitations: Required solution should have a time complexity of O(n), which can be achieved using a stack.
"""


def nextGreatestElement(array):
    stack = []  # Keeps track of indices
    result = [-1] * len(array)  # Initialize the result array with -1

    for i in range(len(array)):
        # While stack is not empty and the current element is greater than the top element in the stack
        while stack and array[i] > array[stack[-1]]:
            index = stack.pop()
            result[index] = array[i]  # The current element is the next greater element for the popped index
        stack.append(i)  # Push the current index onto the stack

    return result


# Test Input
Input = [2, 1, 4, 3]
print(nextGreatestElement(Input))  # Output: [4, 4, -1, -1]
