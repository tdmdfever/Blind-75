"""
Given the roots of two binary trees 'p' and 'q', write a function to check if 
they are the same or not.

Two binary trees are considered the same if they met following two conditions:

Both tree are structurally identical.
Each corresponding node on both the trees have the same value.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if not p and not q:
        return True
    if (p and q and p.val == q.val):
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False

# Test:
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_utils import print_tree

root1 = TreeNode(10)
root1.left = TreeNode(4)
root1.right = TreeNode(15)
root1.left.left = TreeNode(1)
root1.right.left = TreeNode(14)

root2 = TreeNode(10)
root2.left = TreeNode(4)
root2.right = TreeNode(15)
root2.left.left = TreeNode(1)
root2.right.left = TreeNode(14)

print_tree(root1)
print_tree(root2)
print(is_same_tree(root1, root2))