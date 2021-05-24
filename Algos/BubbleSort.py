def BubbleSort(seq):
    if len(seq) <= 1:
        return seq
    
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, len(seq) - 1):

            if seq[i] > seq[i + 1]:
                sorted = False
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    
    return seq

# test code
seq = [4, 1, 6, 2, 7, 9, 3]
print(BubbleSort(seq))

# [1, 2, 3, 4, 6, 7, 9]


# ref
# https://www.youtube.com/watch?v=g_xesqdQqvA