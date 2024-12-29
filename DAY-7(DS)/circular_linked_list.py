class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(24)
n2 = Node(25)
n3 = Node(26)
n4 = Node(27)
n5 = Node(28)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n1

curr = n1
while True:
    print(curr.data, " ", end="")
    curr = curr.next
    if curr == n1:
        break