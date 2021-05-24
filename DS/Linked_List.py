class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value = None):
        self.head = Node(value)

    def insert_at_start(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def print(self):
        if self.head.value is None:
            print("list is empty")
            return

        arr = ""
        itr = self.head
        while itr is not None:
            arr += str(itr.value) + "-->"
            itr = itr.next

        print(arr)

    def append(self, value):
        if self.head.value is None:
            self.head = Node(value)
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next

        itr.next = Node(value)

    def get_length(self):
        if self.head is None:
            return 0

        count = 0
        itr = self.head
        while itr is not None:
            itr = itr.next
            count += 1

        return count

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid Given Index")
        
        if index == 0:
            self.insert_at_start(value)
            return
        
        itr = self.head
        count = 0
        temp = None

        while itr is not None:
            prev = itr
            itr = itr.next
            count += 1

            if count == index:
                new = Node(value)
                new.next = itr
                prev.next = new
                break
        

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid Given Index")
            return

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr is not None:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1


# test code
ll = LinkedList()
ll.print()
ll.append(5)
ll.print()
ll.insert_at_start(3)
ll.append(45)
ll.print()
ll.remove_at(1)
print(f"length of list is : {ll.get_length()}")
ll.print()
ll.append(69)
ll.insert_at(1, 59)
ll.print()

# list is empty
# 5-->
# 3-->5-->45-->
# length of list is : 2
# 3-->45-->
# 3-->59-->45-->69-->


