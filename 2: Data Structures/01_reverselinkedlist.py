"""Given the head of a Singly LinkedList, reverse the LinkedList. Write a 
function to return the new head of the reversed LinkedList."""

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

def reverse(head):
    previous_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

# Test:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
new_head = reverse(head)
while new_head is not None:
    print(new_head.val, end=" ")
    new_head = new_head.next