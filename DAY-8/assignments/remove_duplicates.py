class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return head
    current = head
    seen = set()
    seen.add(current.data)
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return head

# Helper function to print the list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create nodes
N1 = Node(1)
N2 = Node(2)
N3 = Node(1)
N4 = Node(3)
N5 = Node(2)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

print("Original Linked List:")
print_list(N1)

# Remove duplicates
remove_duplicates(N1)

print("Linked List after removing duplicates:")
print_list(N1)