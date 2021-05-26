class BinarySeachTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, value):
        if self.value == value:  # dont add duplicate value
            return

        if value < self.value:
            if self.left:  # if node exists
                self.left.add_child(value)
            else:  # if doesnt exist
                self.left = BinarySeachTree(value)

        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySeachTree(value)

    def max(self):
        if self.right == None:
            return self.value

        return self.right.max()

    def min(self):
        if self.left == None:
            return self.value

        return self.left.min()

    def sum(self):
        return sum(self.inorder())

    # def calculate_sum(self):
    #     left_sum = self.left.calculate_sum() if self.left else 0
    #     right_sum = self.right.calculate_sum() if self.right else 0
    #     return self.data + left_sum + right_sum

    def inorder(self):  # return inorder traversal of the tree (all nodes will be in sorted order)
        nodes = []

        if self.left:  # if left subtree exists
            nodes += self.left.inorder()

        nodes.append(self.value)

        if self.right:
            nodes += self.right.inorder()

        return nodes

    def preorder(self):
        nodes = []

        nodes.append(self.value)
        if self.left:
            nodes += self.left.preorder()
        if self.right:
            nodes += self.right.preorder()

        return nodes

    def postorder(self):
        nodes = []

        
        if self.left:
            nodes += self.left.postorder()
        if self.right:
            nodes += self.right.postorder()

        nodes.append(self.value)
        return nodes

    def search(self, value):
        if self.value == value:  # if found return True
            return True

        if value < self.value:
            if self.left:  # if left subtree exists
                return self.left.search(value)  # return the value

        else:
            if self.right:  # if right subtree exists
                return self.right.search(value)  # return the value

        return  # if not found return None

    def delete(self, value):
        # method is broken
        if value < self.value:
            if self.left:
                self.left.delete(value)

        elif value > self.value:
            if self.right:
                self.right.delete(value)

        
        else:
            # actaul delete logic
            if self.left is None and self.right is None:
                return None

            elif self.left is None and self.right:
                return self.right

            elif self.right is None and self.left:
                return self.left


            rightSubtree_min = self.right.min()
            self.value = rightSubtree_min
            self.right = self.right.delete(rightSubtree_min)

        return self



# test code
bst = BinarySeachTree(5)
bst.add_child(6)
bst.add_child(3)
bst.add_child(7)
bst.add_child(8)
bst.add_child(1)
bst.add_child(9)
print(bst.inorder())

bst.delete(5)
print(bst.max())
print(bst.min())
print(bst.sum())
print()
print(bst.preorder())
print(bst.postorder())

print("deleting 3")
bst.delete(3)
print(bst.inorder())

# [1, 3, 5, 6, 7, 8, 9]
# 9
# 1
# 34

# [6, 3, 1, 7, 8, 9]
# [1, 3, 9, 8, 7, 6]
# deleting 3
# [1, 3, 6, 7, 8, 9]

"""
ref:
https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10
"""
