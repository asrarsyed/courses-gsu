# Course Section: CSC 2720-012

"""
Assignment: Implement Round Robin scheduling algorithm using a circular linked list
"""


class Node:
    def __init__(self, pid, burstTime):
        self.pid = pid
        self.burstTime = burstTime
        self.next = None


class CircularLinkedList:  # Initialize an empty circular linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, pid, burstTime):  # Add a new process to the circular linked list
        if not (1 <= burstTime <= 100):
            raise ValueError("Burst time must be between 1 and 100")

        new_node = Node(pid, burstTime)

        if not self.head:  # First process in the list
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:  # Add to end and maintain circular structure
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def remove(self, prev_node, node):  # Remove a completed process from the list
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
            return

        if node == self.head:  # Removing head
            self.tail.next = self.head.next
            self.head = self.head.next
        elif node == self.tail:  # Removing tail
            prev_node.next = self.head
            self.tail = prev_node
        else:  # Removing from middle
            prev_node.next = node.next

    def display(self):  # Display all processes and their remaining burst times
        if not self.head:
            print("No processes in the list")
            return

        print("\nProcesses in the list:")
        current = self.head
        while True:
            print(f"Process {current.pid}: Remaining Burst Time = {current.burstTime}")
            current = current.next
            if current == self.head:
                break

    def is_empty(self):
        """Check if all processes are completed"""
        return self.head is None


def round_robin_scheduler(processes, quantum_time):  # Round Robin scheduling algorithm, returns total time
    # Validate the inputs
    if not (1 <= len(processes) <= 50):
        raise ValueError("Number of processes must be between 1 and 50")
    if not (1 <= quantum_time <= 10):
        raise ValueError("Time quantum must be between 1 and 10")

    # Initialize circular linked list
    process_list = CircularLinkedList()
    for pid, burstTime in processes:
        process_list.append(pid, burstTime)

    total_time = 0
    process_list.display()

    # Continue until all processes are completed
    current = process_list.head
    prev = process_list.tail

    while not process_list.is_empty():
        if current.burstTime <= quantum_time:
            # Process will complete in this quantum
            total_time += current.burstTime
            next_process = current.next
            process_list.remove(prev, current)
            print(f"\nTime {total_time}: Process {current.pid} completed")

            if process_list.is_empty():
                break

            current = next_process
            if prev.next == current:
                prev = prev
            else:
                prev = process_list.tail

        else:
            # Process needs more time
            current.burstTime -= quantum_time
            total_time += quantum_time
            print(f"\nTime {total_time}: Process {current.pid} used quantum")
            process_list.display()

            prev = current
            current = current.next

    return total_time
