"""
Given two binary trees s and t, determine if tree t is a subtree of tree s. 
A tree t is considered a subtree of s if there exists a node in s such that 
the subtree of that node is identical to t. Both trees are considered identical 
if their structure and nodes are the same.

Example 1:
Input:
Tree s: [3,4,5,1,2]
Tree t: [4,1,2]
Expected Output: true
Justification: Tree t can be found as a subtree of s rooted at the node with value 4.

Example 2:
Input:
Tree s: [1,2,3]
Tree t: [2,3]
Expected Output: false
Justification: There's no subtree in s that looks like tree t.

Example 3:
Input:
Tree s: [3,4,5,1,2,null,null,null,null,0]
Tree t: [4,1,2]
Expected Output: false
Justification: Even though there's a subtree with root 4, it's not identical to tree t.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(s, t):
    def is_same_tree(p, q):
        if not p and not q:
            return True
        if (p and q and p.val == q.val):
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        else:
            return False

    queue = deque([s])
    while queue:
        node = queue.popleft()
        if node:
            queue.extend([node.left, node.right])
            if node.val == t.val and is_same_tree(node, t):
                return True
    return False

# Test:
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_utils import print_tree

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subroot = TreeNode(4)
subroot.left = TreeNode(1)
subroot.right = TreeNode(2)

print_tree(root, 0, "Root: ")
print_tree(subroot, 0, "Subroot: ")
print(is_subtree(root, subroot))