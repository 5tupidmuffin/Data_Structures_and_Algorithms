def BinarySearch(seq, value):
    """
    Args:
        seq (list): list of sorted elements
        value (Any): item to be searched

    Returns:
        index(int): index at which the value is present
    """
    
    left = 0
    right = len(seq) - 1
    mid = 0  # no need to initialize
    
    while left <= right:
        mid = (left + right) // 2  # to find mid of remaining items
        mid_value = seq[mid]

        if value == mid_value:
            return mid

        if value < mid_value:
            right = mid - 1

        elif value > mid_value:
            left = mid + 1

    return None  # if value is not present in seq

seq = [1, 4, 6, 9, 14, 16]
item = 9


# test code
print(f"{item} is present at {BinarySearch(seq, item)} index position")

# 9 is present at 3 index position