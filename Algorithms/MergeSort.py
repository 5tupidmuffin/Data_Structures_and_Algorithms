def merge(left, right):
    i = j = 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    while i < len(left):
        sorted.append(left[i])
        i += 1

    while j < len(right):
        sorted.append(right[j])
        j += 1

    return sorted


def mergeSort(seq):
    if len(seq) <= 1:
        return seq
    

    middle = len(seq) // 2

    left = seq[:middle]
    right = seq[middle:]


    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


# test code
seq = [38, 27, 43, 3, 9, 82, 10]
print(mergeSort(seq))

# [3, 9, 10, 27, 38, 43, 82]

"""
ref:
    https://www.youtube.com/watch?v=nCNfu_zNhyI
"""