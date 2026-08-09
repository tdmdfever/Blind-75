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
