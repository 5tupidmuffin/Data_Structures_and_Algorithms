class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()
        self.parent = None

    def add_chid(self, node):
        node.parent = self  # make self as parent
        self.children.append(node)  # add child in the children lists

    def get_level(self):
        # just to for pretty print
        level = 0
        p = self.parent
        while p: # if parent exits
            level += 1
            p = p.parent

        return level

    def print_tree(self):  # fancy preorder print
        spaces = "  " * self.get_level()  # higher the level more space
        prefix = spaces + "|--" if self.parent else ""  # if else statement so as to avoid printing "|--" brefore root
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


# test code
root = TreeNode("electronics")

laptop = TreeNode("laptop")
lenovo = TreeNode("lenovo")
laptop.add_chid(lenovo)
hp = TreeNode("hp")
laptop.add_chid(hp)

tv = TreeNode("tv")
sam = TreeNode("sam")
lg = TreeNode("lg")
tv.add_chid(sam)
tv.add_chid(lg)

phone = TreeNode("phone")
samsung = TreeNode("samsung")
apple = TreeNode("apple")
phone.add_chid(samsung)
phone.add_chid(apple)

root.add_chid(laptop)
root.add_chid(tv)
root.add_chid(phone)

root.print_tree()


# electronics
#   |--laptop
#     |--lenovo
#     |--hp
#   |--tv
#     |--sam
#     |--lg
#   |--phone
#     |--samsung
#     |--apple

"""
ref:
https://www.youtube.com/watch?v=4r_XR9fUPhQ&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=9
"""







