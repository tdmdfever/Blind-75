"""
Given a linked list, remove the last nth node from the end of the list and 
return the head of the modified list.

Example 1:
Input: list = 1 -> 2 -> 3 -> 4 -> 5, n = 2
Expected Output: 1 -> 2 -> 3 -> 5
Justification: The 2nd node from the end is "4", so after removing it, the list becomes [1,2,3,5].

Example 2:
Input: list = 10 -> 20 -> 30 -> 40, n = 4
Expected Output: 20 -> 30 -> 40
Justification: The 4th node from the end is "10", so after removing it, the list becomes [20,30,40].

Example 3:
Input: list = 7 -> 14 -> 21 -> 28 -> 35, n = 3
Expected Output: 7 -> 14 -> 28 -> 35
Justification: The 3rd node from the end is "21", so after removing it, the list becomes [7,14,28,35].
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth(head, n):
    current_node = head
    counter = 0
    ledger = {}
    while current_node != None:
        ledger[counter] = current_node
        current_node = current_node.next
        counter += 1
        
    if counter == n:
        new_head = head.next
        head.next = None
        return new_head
    else:
        position = counter - n
        ledger[position - 1].next = ledger[position].next
        ledger[position].next = None

    return head

# Test:
node1, node2, node3, node4, node5 = Node(1), Node(2), Node(3), Node(4), Node(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print(remove_nth(node1, 2))
current_node = node1
while current_node != None:
    print(current_node.val)
    current_node = current_node.next

