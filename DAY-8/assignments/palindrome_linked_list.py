class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Compare the first and second halves
    first_half = head
    second_half = prev
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = next_node

    return True

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
N3 = Node(2)
N4 = Node(1)
N1.next = N2
N2.next = N3
N3.next = N4

print("Original Linked List:")
print_list(N1)

# Check if the linked list is a palindrome
result = is_palindrome(N1)
print("Is the linked list a palindrome?", result)