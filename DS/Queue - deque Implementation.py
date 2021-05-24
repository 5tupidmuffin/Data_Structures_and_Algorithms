"""
using deque instead of list because it is memory efficient
"""
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()

    def __str__(self):
        return str(list(self.buffer))


# test code
q = Queue()
q.enqueue(2)
q.enqueue(5)
print(q)
print("removing", q.dequeue())
print(q)

# [5, 2]
# removing 2
# [5]



