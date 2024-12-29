class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None   

class Binary_search_tree:
    def __init__(self):
        self.root = None
        def insert(self, data):
            if self.root is None:
                self.root = Node(data)
            else:
                self._insert(data, self.root)
    def insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Value is already present in the tree.")
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")
bst = Binary_search_tree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(20)

print("In-order traversal:")
bst.in_order(bst.root)
print("\nPre-order traversal:")
bst.pre_order(bst.root)
print("\nPost-order traversal:")
bst.post_order(bst.root)
            