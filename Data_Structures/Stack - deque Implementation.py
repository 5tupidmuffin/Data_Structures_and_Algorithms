"""
using deque because python's list is not memory effiecient when used as stack since its a dynamic array which will alot 2 capacity if initial capacity is filled
deque is a doubly linked list so its memory efficient and it comes with python
"""
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()  # a container deque object for stack

    def is_empty(self):
        # return True if stack is empty
        return len(self.stack) == 0

    def peek(self):
        # returns last element from the stack
        if not self.is_empty():
            return self.stack[-1]

    def push(self, value):
        # adds element to the stack
        self.stack.append(value)

    def pop(self):
        # removes and returns last element from the stack
        if not self.is_empty():
            return self.stack.pop()


# test code
s = Stack()
print(s.is_empty())
print(s.peek())
s.push(1)
s.push(2)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())

# True
# None
# 2
# 2
# 1
# None


"""
ref:
https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7
"""

