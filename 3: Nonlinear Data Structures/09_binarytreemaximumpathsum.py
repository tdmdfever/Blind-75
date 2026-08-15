"""
Find the path with the maximum sum in a given binary tree. Write a function 
that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and 
doesn't necessarily pass through the root. The path must contain at least 
one node.
"""

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_maximum_path_sum(root):
    global_maximum_sum = -math.inf
    
    def maximum_path_sum_at(node):
        nonlocal global_maximum_sum
        if not node:
            return 0

        left_gain = max(maximum_path_sum_at(node.left), 0)
        right_gain = max(maximum_path_sum_at(node.right), 0)

        global_maximum_sum = max(global_maximum_sum, node.val + left_gain + right_gain)

        return node.val + max(left_gain, right_gain)

    maximum_path_sum_at(root)
    return global_maximum_sum

# Test:
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_utils import print_tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(9)

print_tree(root)
print(find_maximum_path_sum(root))