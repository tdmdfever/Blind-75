# Remove nth node from end of linked list

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

"""
node1, node2, node3, node4, node5 = Node(1), Node(2), Node(3), Node(4), Node(5)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
print(removeNth(node1, 2))
current_node = node1
while current_node != None:
    print(current_node.val)
    current_node = current_node.next
"""
