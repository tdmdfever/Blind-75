"""
Determine if a given binary tree is a binary search tree (BST). In a BST, for 
each node:

All nodes to its left have values less than the node's value.
All nodes to its right have values greater than the node's value.

Example 1:
Input: [5,3,7]
Expected Output: true
Justification: The left child of the root (3) is less than the root, and the right child of the root (7) is greater than the root. Hence, it's a BST.

Example 2:
Input: [5,7,3]
Expected Output: false
Justification: The left child of the root (7) is greater than the root, making it invalid.

Example 3:
Input: [10,5,15,null,null,12,20]
Expected Output: true
Justification: Each subtree of the binary tree is a valid binary search tree. So, a whole binary tree is a valid binary search tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    if not root:
        return True
        
    if (root.left and root.val <= root.left.val) or (root.right and root.val >= root.right.val):
        return False
    if not (is_valid_bst(root.left) and is_valid_bst(root.right)):
        return False

    return True

# Test:
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_utils import print_tree

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

print_tree(root)
print(is_valid_bst(root))