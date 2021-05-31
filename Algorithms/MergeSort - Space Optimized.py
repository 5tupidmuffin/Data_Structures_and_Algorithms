"""
modifying the given array instead of creating a new one at every call

"""

def merge(left, right, seq):
    i = j = k = 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            seq[k] = left[i]
            i += 1
            k += 1
        else:
            seq[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        seq[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        seq[k] = right[j]
        k += 1
        j += 1


def mergeSort(seq):
    if len(seq) <= 1:
        return
    

    middle = len(seq) // 2

    left = seq[:middle]
    right = seq[middle:]


    mergeSort(left)
    mergeSort(right)

    merge(left, right, seq)


# test code
seq = [38, 27, 43, 3, 9, 82, 10]
mergeSort(seq)
print(seq)

# [3, 9, 10, 27, 38, 43, 82]

"""
ref:
    https://www.youtube.com/watch?v=nCNfu_zNhyI
"""