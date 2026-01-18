from utils import ArrayStack


class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def transfer(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            self.transfer()
        if self.stack2.is_empty():
            raise IndexError("Queue is empty!")

        return self.stack2.pop()

    def front(self):
        if self.stack2.is_empty():
            self.transfer()
        if self.stack2.is_empty():
            raise IndexError("Queue is empty!")

        return self.stack2.top()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)


q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.front()

q.enqueue(4)
q.enqueue(5)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.front())
