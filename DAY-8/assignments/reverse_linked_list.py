class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Create nodes
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N1.next = N2
N2.next = N3

# Print original list
current = N1
while current:
    print(current.data, end="->")
    current = current.next
print("None")

# Reverse the list
reversed_head = reverse_list(N1)

# Print reversed list
current = reversed_head
while current:
    print(current.data, end="->")
    current = current.next
print("None")
