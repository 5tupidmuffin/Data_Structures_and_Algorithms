class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def add_child(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = add_child(root.left, value)

    elif value > root.value:
        root.right = add_child(root.right, value)

    return root


def inorder(root):
    nodes = []

    if root.left:
        nodes += inorder(root.left)

    nodes.append(root.value)

    if root.right:
        nodes += inorder(root.right)

    return nodes


def max(root):
    if root.right:
        return max(root.right)

    return root

def min(root):
    if root.left:
        return min(root.left)

    return root

def search(root, value):
    if root.value == value:
        return True

    elif value < root.value:
        if root.left:
            return search(root.left, value)

    elif value > root.value:
        if root.right:
            return search(root.right, value)

def delete(root, value):
    # function is broken
    if root is None:
        return None

    if value < root.value:
        if root.left:
            delete(root.left, value)

    elif value > root.value:
        if root.right:
            delete(root.right, value)

    else:
        # if node has no child
        if root.left is None and root.right is None:
            root = None
            return None

        # if node has one child
        elif root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if node has 2 childs
        temp = min(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    return root


# test code
root = Node(3)
add_child(root, 2)
add_child(root, 5)
add_child(root, 4)
add_child(root, 6)

print(inorder(root))

delete(root, 2)
print(inorder(root))


# [2, 3, 4, 5, 6]
# [2, 3, 4, 5, 6]



"""
ref:
https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
"""