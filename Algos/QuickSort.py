def QuickSort(seq):
    if len(seq) <= 1:
        return seq
    
    lower = list()
    higher = list()
    pivot = seq.pop()

    for item in seq:
        if item > pivot:
            higher.append(item)
        else:
            lower.append(item)
    
    return QuickSort(lower) + [pivot] + QuickSort(higher)

# test code
seq = [4, 1, 6, 2, 7, 9, 3]
print(QuickSort(seq))

# [1, 2, 3, 4, 6, 7, 9]


# ref
# https://www.youtube.com/watch?v=kFeXwkgnQ9U