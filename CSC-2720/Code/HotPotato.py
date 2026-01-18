from utils import ArrayQueue


def hotPotato(names, count):
    q = ArrayQueue()
    for name in names:
        q.enqueue(name)
    round = 1
    while q.size() > 1:
        for i in range(count):
            q.enqueue(q.dequeue())
        print("Round", round, ":", q.front(), "is eliminated.")
        round += 1
        q.dequeue()

    return q.dequeue()


print("Winner:", hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 5))
