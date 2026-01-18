class CustomStack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def is_empty(self):
        return len(self._data) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def top(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def __len__(self):
        return len(self._data)


stack = CustomStack()
