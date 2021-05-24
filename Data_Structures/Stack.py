class Stack:
    # list implementation of stack
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        # return len of the stack
        return len(self.stack) == 0
    
    def peek(self):
        # return last element of the stack
        if len(self.stack) == 0:
            print("stack is epmty")
            return
        
        return self.stack[-1]
    
    def push(self, value):
        # add an element to the stack
        self.stack.append(value)
    
    def pop(self):
        # delete last added element from the stack
        if len(self.stack) == 0:
            print("stack is empty")
            return
        
        return self.stack.pop()
 

# test code 
test = Stack()

last = test.peek()
test.push(2)
test.push(3)
last = test.peek()
print(test.is_empty())
test.pop()
test.pop()
test.pop()

# stack is epmty
# False
# stack is empty

"""
ref:
https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7
"""

