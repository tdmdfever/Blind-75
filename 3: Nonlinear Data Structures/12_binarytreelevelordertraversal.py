"""
Given a binary tree, populate an array to represent its level-by-level 
traversal. You should populate the values of all nodes of each level from left 
to right in separate sub-arrays.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(root):
    result = []
    queue = deque([(0, root)])
    while queue:
        (level, node) = queue.popleft()
        if node:
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)
            queue.extend([(level + 1, node.left), (level + 1, node.right)])

    return result

# Test:
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_utils import print_tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print_tree(root)
print(traverse(root))