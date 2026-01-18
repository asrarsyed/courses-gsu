# Course Section: CSC 2720-012

class array:
    """
    Implement two stacks within a single Python list.
    The first stack will start from the beginning of the list (left stack), and the second will start from the end (right stack). 
        
    Notes: 
        Handle the 'Stack Overflow' situation gracefully.
        Handle the 'Stack Underflow' situation gracefully.
    """

    def __init__(self, n): 
        """  initialize the ‘Two Stacks’ object. Here ‘n’ is the total number of items that both stacks can hold. """
        self.size = n
        self.array = [None] * n
        self.leftIndex = -1  # Top pointer for left stack - starts at index 0, grows to the right
        self.rightIndex = n  # Top pointer for right stack - starts at index n-1, grows to the left

    def push_left(self, item):
        """  pushes the item onto the left stack. """
        if self.leftIndex < self.rightIndex - 1:
            self.leftIndex += 1
            self.array[self.leftIndex] = item
        else:
            print("Cannot push onto left stack due to Stack Overflow")

    def push_right(self, item):
        """  pushes the item onto the right stack. """
        if self.leftIndex < self.rightIndex - 1:
            self.rightIndex -= 1
            self.array[self.rightIndex] = item
        else:
            print("Cannot push onto right stack due to Stack Overflow")

    def pop_left(self):
        """  pops the top item from the left stack. """
        if self.leftIndex >= 0:
            popped_item = self.array[self.leftIndex]
            self.leftIndex -= 1
            return popped_item
        else:
            print("Left stack is empty due to Stack Underflow")
            return None

    def pop_right(self):
        """  pops the top item from the right stack.. """
        if self.rightIndex < self.n:
            popped_item = self.array[self.rightIndex]
            self.rightIndex += 1
            return popped_item
        else:
            print("Right stack is empty due to Stack Underflow")
            return None

    def len_left(self):
        """  returns the number of items in the left stack. """
        return self.leftIndex + 1

    def len_right(self):
        """  returns the number of items in the right stack. """
        return self.n - self.rightIndex