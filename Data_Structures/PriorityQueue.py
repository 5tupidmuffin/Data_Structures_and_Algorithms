"""
python list not very efficient for priority queue since it reqiures sorting after each enque
Priority Queue deos this itselt, 
lowest value --> high priority
"""

from queue import PriorityQueue as pq  # naming it pq so as to avoid confusion

class PriorityQueue:
    def __init__(self):
        self.container = pq()

    def size(self):
        return self.container.qsize()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.container.put(value)

    def dequeue(self):
        if not self.is_empty():
            return self.container.get()



# test code
test = PriorityQueue()
print(test.is_empty())
test.enqueue(2)
test.enqueue(1)
test.enqueue(10)
print(test.is_empty())
print(test.container)
print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
print(test.container)
print(test.is_empty())

# True
# False
# <queue.PriorityQueue object at 0x000002B023879AF0>
# 1
# 2
# 10
# <queue.PriorityQueue object at 0x000002B023879AF0>
# True

