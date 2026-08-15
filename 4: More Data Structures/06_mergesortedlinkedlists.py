"""
Given an array of 'K' sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""

import heapq

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.val < other.val


def merge(lists):
    min_heap = []

    for i, head in enumerate(lists):
        if head:
            heapq.heappush(min_heap, (head.val, i, head))

    dummy = ListNode(0)
    current_node = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current_node.next = node
        current_node = current_node.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

# Test:
l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)
l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)
l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

merged_head = merge([l1, l2, l3])
current = merged_head
while current:
    print(current.val, end=" ")
    current = current.next