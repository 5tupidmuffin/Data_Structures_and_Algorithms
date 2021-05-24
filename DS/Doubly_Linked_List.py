class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value = None):
        self.head = None

    def print(self):
        if self.head is None:
            print("list is empty")
            return

        arr = ""
        itr = self.head
        while itr is not None:
            arr += "<--" + str(itr.value) + "-->"
            itr = itr.next

        print(arr)

    def insert_at_start(self, value):
        if self.head == None:
            self.head = Node(value)
            return


        new = Node(value)
        new.next = self.head
        self.head.prev = new
        self.head = new
        return


    def append(self, value):
        if self.head is None:
            self.insert_at_start(value)
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next

        new = Node(value)
        new.prev = itr
        itr.next = new
        return

    def get_length(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        count = 0

        while itr is not None:
            itr = itr.next
            count += 1

        return count

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid Index")

        if index == 0:
            self.insert_at_start(value)
            return

        itr = self.head
        count = 0
        while itr is not None:
            if count == index:
                new = Node(value)
                itr.prev.next = new
                new.prev = itr.prev
                new.next = itr
                itr.prev = new
                return

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr is not None:
            if count == index:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                return
            itr = itr.next
            count += 1

# test code
ll = DoublyLinkedList()
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
ll.insert_at(1, 95)
ll.print()

# list is empty
# <--5-->
# <--3--><--5--><--45-->
# length of list is : 2
# <--3--><--45-->
# <--3--><--95--><--45--><--69-->


