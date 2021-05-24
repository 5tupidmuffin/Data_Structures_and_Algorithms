"""
we mostly use python dictionary for hashtable this code is just for the sake of understanding how hashtable actually works
"""

class HashTable:
    def __init__(self):
        self.MAX = 100  # max item count to create an list
        self.arr = [None for i in range(self.MAX)]  # actual array of None items

    def get_hash(self, key):  # a function to convert string into logical index
        keyhash = 0
        for i in key:
            keyhash += ord(i)  # ord(test) function ord returns the ascii value of test

        return (keyhash % self.MAX)  # we find modulus so as to fit the item in the array

    def __setitem__(self, key, value):  # special python function
        key = self.get_hash(key)
        self.arr[key] = value

    def __getitem__(self, key):  # special python function
        key = self.get_hash(key)
        return self.arr[key]

    def __delitem__(self, key):  # special python function
        key =self.get_hash(key)
        self.arr[key] = None


# test code
table = HashTable()
table['april 1'] = 100
print(table['april 1'])
del table['april 1']  # 'del' for delete an item
print(table['april 1'])

# 100
# None


"""
ref
https://www.youtube.com/watch?v=ea8BRGxGmlA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=5
https://docs.python.org/3/library/operator.html    # python special operator functions 
"""