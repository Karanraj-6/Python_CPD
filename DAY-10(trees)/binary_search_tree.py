class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
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

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, current_node):
        if current_node is None:
            return False
        elif data < current_node.data:
            return self._search(data, current_node.left)
        elif data > current_node.data:
            return self._search(data, current_node.right)
        else:
            return True

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
    def height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1   
        
    def leaf_node(self, node):
        if node is None:
            return 1
        if node.left is None and node.right is None:
            return 1
        else:
            return self.leaf_node(node.left) + self.leaf_node(node.right)
    def sum_of_nodes(self,node):
        # if node is None:
        #     return node.data
        if node.left is None:
            return node.data
        elif node.right is  None:
            return node.data
        else:
            return self.sum_of_nodes(node.left) + self.sum_of_nodes(node.right)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(12)
bst.insert(11)
bst.insert(17)


print("In-order traversal:")
bst.in_order(bst.root)
print("\nPre-order traversal:")
bst.pre_order(bst.root)
print("\nPost-order traversal:")
bst.post_order(bst.root)

# Search for elements
print("\nSearch for elements:")
print("Search 7:", bst.search(7))  # Output: True
print("Search 14:", bst.search(14))  # Output: False

print("Height of the tree:", bst.height(bst.root))  # Output: 2
print("No of leaf nodess:" , bst.leaf_node(bst.root))
print("Sum of Node :", bst.sum_of_nodes(bst.root))