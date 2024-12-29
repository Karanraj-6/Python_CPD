class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midlle_element(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

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

# Find the middle element
middle = midlle_element(N1)
print("Middle element:", middle)