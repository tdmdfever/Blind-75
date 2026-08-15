"""
Given a root node of the binary tree, return the depth (or height) of a binary 
tree.

The Depth of the binary tree refers to the number of nodes along the 
longest path from the root node to the farthest leaf node. If the tree is 
empty, the depth is 0.

Example 1:
Input: root = [1, 2, 3, 4, 5]
Expected Output: 3
Explanation: The longest path is 1->2->4 or 1->2->5 with 3 nodes.

Example 2:
Input: root = [1, null, 2, null, 3]
Expected Output: 3
Justification: There's only one path 1->2->3 with 3 nodes.

Example 3:
Input: root = [1, 2, 3, 4, 7, null, null, null, null, null, 9]
Expected Output: 4
Justification: The longest path is 1->2->7->9 with 4 nodes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))

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

print_tree(root)
print(max_depth(root))