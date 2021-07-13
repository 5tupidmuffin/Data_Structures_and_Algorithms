def insertionSort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        vacant = i

        while vacant > 0 and seq[vacant - 1] > key:
            seq[vacant] = seq[vacant - 1]
            vacant -= 1

        seq[vacant] = key

def insertionSort2(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1

        while j >= 0 and seq[j] > key:
            seq[j + 1] = seq[j]
            j -= 1

        seq[j + 1] = key

def reverse(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        
        while j >= 0 and key > seq[j]:
            seq[j + 1] = seq[j]
            j -= 1

        seq[j + 1] = key

arr = [2, 1, 4, 0]
insertionSort(arr)
print(arr)
# [0, 1, 2, 4]

"""
time complexity: O(n^2)
space complexity: O(1)  # inplace
https://www.youtube.com/watch?v=i-SKeOcBwko
"""