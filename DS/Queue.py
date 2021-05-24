class Queue:
    def __init__(self):
        self.buffer = list()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return self.size() == 0


    def enqueue(self, value):
        self.buffer.insert(0, value)

    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()

    def __str__(self):
        return str(self.buffer)

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

"""
ref:
https://www.youtube.com/watch?v=rUUrmGKYwHw&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=8
"""
