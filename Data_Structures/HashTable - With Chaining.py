"""
we mostly use python dictionary for hashtable this code is just for the sake of understanding how hashtable actually works
implementing chaining in this code so as to tackle collision where 2 different key can end up having same hash value
"""

class HashTable:
    def __init__(self):
        self.MAX = 100  # max item count to create an list
        self.arr = [[] for i in range(self.MAX)]  # actual array of list so as to store multiple (key, value) pair at same index

    def get_hash(self, key):  # a function to convert string into logical index
        keyhash = 0
        for i in key:
            keyhash += ord(i)  # ord(test) function ord returns the ascii value of test

        return (keyhash % self.MAX)  # we find modulus so as to fit the item in the array

    def __setitem__(self, key, value):  # special python function
        hashvalue = self.get_hash(key)
        for k, val in self.arr[hashvalue]:
            # if key already exist in the given index change the related value
            if key == k:
                val = value
                return

        self.arr[hashvalue].append([key, value])  # if the key doenst exist add a new pair
        return
        

    def __getitem__(self, key):  # special python function
        hashvalue = self.get_hash(key)

        if len(self.arr[hashvalue]) == 0:
            return None

        if len(self.arr[hashvalue]) == 1:
            return self.arr[hashvalue][0][1] # 0th element's 1'st element ref. [[key, value]] we return the value

        for k, val in self.arr[hashvalue]:
            if k == key:
                return val

        

    def __delitem__(self, key):  # special python function
        hashvalue =self.get_hash(key)
        
        if len(self.arr[hashvalue]) == 0:
            return 

        if len(self.arr[hashvalue]) == 1:
            self.arr[hashvalue] = []  # overwrite with an empty list
            return

        for i in range(len(self.arr[hashvalue])):
            if i[0] == key:  # if k is equal to the given index
                self.arr[hashvalue].pop(i)
                return






# test code
table = HashTable()
table['april 1'] = 100
print(table['april 1'])
del table['april 1']  # 'del' for delete an item
print(table['april 1'])
table['march 6'] = 85 
table['march 17'] = 69  # hash value will be same as 'march 6'
print(table['march 6'])
print(table['march 17'])
del table['march 6']
print(table['march 6'])  # only 'march 6' has to be deleted
print(table['march 17'])  # only 'march 6' was deleted


# 100
# None
# 85
# 69
# None
# 69

"""
ref
https://www.youtube.com/watch?v=ea8BRGxGmlA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=5
https://docs.python.org/3/library/operator.html    # python special operator functions 
"""