def selectionSort(seq):
    for i in range(len(seq)):
        min = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[min]:
                seq[j], seq[min] = seq[min], seq[j]

# test code
seq = [3, 2, 1, 6, 5, 8, 7]
selectionSort(seq)
print(seq)

# [1, 2, 3, 5, 6, 7, 8]

"""
ref:
    https://www.youtube.com/watch?v=hhkLdjIimlw
"""

