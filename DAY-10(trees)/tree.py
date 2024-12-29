class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            new_node = BinaryTree(data)
            new_node.right = self.right
            self.right = new_node

    def pre_order(self):
        print(self.data, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data, end=" ")
        


n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)

n1.insert_left(2)
n1.insert_right(3)
n1.left.insert_left(4)
n1.left.insert_right(5)

print("Pre-order traversal:")
n1.pre_order()
print("\nIn-order traversal:")
n1.in_order()
print("\nPost-order traversal:")
n1.post_order()