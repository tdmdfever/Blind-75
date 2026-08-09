import heapq

class ListNode:
  def __init__(self, value):
    self.val = value
    self.next = None

# used for the min-heap
  def __lt__(self, other):
    return self.val < other.val


def merge(lists):
    minheap = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(minheap, (l.val, i, l))
    
    dummy = ListNode(0)
    current_node = dummy

    while minheap:
        val, i, node = heapq.heappop(minheap)
        current_node.next = node
        current_node = current_node.next

        if node.next: 
            heapq.heappush(minheap, (node.next.val, i, node.next))

    return dummy.next