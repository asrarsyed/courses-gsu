# Course Section: CSC 2720-012

from queue import Queue


class StackInAQueue:
    """
    Key Ideas:
        For a stack, the last element inserted is the first to be removed (LIFO).
        For a queue, the first element inserted is the first to be removed (FIFO).

    Goals:
    To simulate stack behavior using a queue.
    The underlying data should be maintained in a queue (not an array/list/deque).
    The class should contain the following methods:
        - push(item)
        - pop()
        - __len__()
        - top()
    """

    def __init__(self):
        self._queue = Queue()

    def push(self, item):  # This adds an item to a queue and then rotates the queue so the new item is at the front
        size = self._queue.qsize()
        self._queue.put(item)
        for _ in range(size):
            self._queue.put(self._queue.get())

    def pop(self):  # Uses the imported queues internal methods, to check empty and to remove.
        if self._queue.empty():
            raise IndexError("Trying to pop from an empty stack!")
        return self._queue.get()

    def __len__(self):  # Uses the imported queues internal methods, to check empty and to get lenght of queue.
        return self._queue.qsize()

    def top(self):  # Uses the imported queues internal methods, to check empty and to remove and put into queue
        if self._queue.empty():
            raise IndexError("The stack is empty!")

        top_item = self._queue.get()
        self._queue.put(top_item)

        for _ in range(self._queue.qsize() - 1):
            self._queue.put(self._queue.get())
        return top_item

    def push_k_items(self, items):
        if len(items) > len(self):
            raise ValueError("Cannot push more items than the current size of the stack!")

        for item in items:
            self._queue.put(item)

        for _ in range(self._queue.qsize() - len(items)):
            self._queue.put(self._queue.get())
