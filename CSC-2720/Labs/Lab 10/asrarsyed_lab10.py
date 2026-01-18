# Course Section: CSC 2720-012

"""
Assignment: Write a Python class that uses priority queues and provides the  following functionalities:

Note: - You may use the ‘heapq’ module.
      - Be sure to include driver code to test your application.
"""

import heapq


class TaskManager:
    def __init__(self):
        # Initialize the task manager with an empty priority queue and task lookup.
        self._heap = []
        self._lookup = {}
        self._counter = 0

    def add_task(self, task_name, priority_level):
        # Adds a task to the heap with the specified priority level (lower number = higher priority).
        if not isinstance(task_name, str) or not isinstance(priority_level, int):
            raise ValueError(
                "Task name must be a string and priority must be an integer"
            )

        entry = (priority_level, self._counter, task_name)
        heapq.heappush(self._heap, entry)

        if task_name not in self._lookup:
            self._lookup[task_name] = []
        self._lookup[task_name].append((priority_level, self._counter))
        self._counter += 1

    def get_most_urgent_task(self):
        # Returns the name of the task with the highest priority.
        if not self._heap:
            return None
        return self._heap[0][2]

    def finish_most_urgent_task(self):
        # Returns the name of the task with the highest priority and removes it from the heap.
        if not self._heap:
            return None

        priority, counter, task_name = heapq.heappop(self._heap)
        self._lookup[task_name].remove((priority, counter))
        if not self._lookup[task_name]:
            del self._lookup[task_name]
        return task_name

    def get_next_n_tasks(self, n):
        # Returns the next n tasks with the highest priority.
        if n <= 0:
            return []

        # Create a copy of the heap to avoid modifying the original
        temp_heap = self._heap.copy()
        result = []

        for _ in range(min(n, len(temp_heap))):
            entry = heapq.heappop(temp_heap)
            result.append(entry[2])

        return result

    def get_last_n_tasks(self, n):
        # Returns n tasks with the lowest priority.
        if n <= 0:
            return []

        # Sort heap by priority (descending) and get last n items
        sorted_tasks = sorted(self._heap, reverse=True)
        return [task[2] for task in sorted_tasks[:n]]

    def change_priority(self, task_name, new_priority):
        # Update the priority of ‘task’ to ‘new_priority’.
        if task_name not in self._lookup:
            return False

        # Remove all instances of the task from the heap
        self._heap = [entry for entry in self._heap if entry[2] != task_name]
        heapq.heapify(self._heap)

        # Add the task back with the new priority
        for _ in range(len(self._lookup[task_name])):
            self.add_task(task_name, new_priority)

        return True

    def __len__(self):
        # Return the number of tasks in the queue.
        return len(self._heap)


# Driver code to test the TaskManager
def test_task_manager():
    tm = TaskManager()

    # Test adding tasks
    print("Adding tasks...")
    tm.add_task("Task 1", 2)
    tm.add_task("Task 2", 1)
    tm.add_task("Task 3", 2)
    tm.add_task("Task 4", 3)
    print(f"Total tasks: {len(tm)}")

    # Test getting most urgent task
    print("\nMost urgent task:", tm.get_most_urgent_task())

    # Test getting next 3 tasks
    print("\nNext 3 tasks:", tm.get_next_n_tasks(3))

    # Test getting last 2 tasks (lowest priority)
    print("\nLast 2 tasks:", tm.get_last_n_tasks(2))

    # Test finishing most urgent task
    finished_task = tm.finish_most_urgent_task()
    print(f"\nFinished task: {finished_task}")
    print(f"Remaining tasks: {len(tm)}")

    # Test changing priority
    print("\nChanging priority of 'Write report' to 1...")
    tm.change_priority("Write report", 1)
    print("New most urgent task:", tm.get_most_urgent_task())


if __name__ == "__main__":
    test_task_manager()
