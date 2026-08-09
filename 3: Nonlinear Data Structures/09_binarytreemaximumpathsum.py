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

def findMaximumPathSum(root):
    globalMaximumSum = -math.inf
    
    def maximumPathSumAt(node):
        nonlocal globalMaximumSum
        if not node:
            return 0

        left_gain = max(maximumPathSumAt(node.left), 0)
        right_gain = max(maximumPathSumAt(node.right), 0)

        globalMaximumSum = max(globalMaximumSum, node.val + left_gain + right_gain)

        return node.val + max(left_gain, right_gain)

    maximumPathSumAt(root)
    return globalMaximumSum

# Test:
def print_tree(root, level=0, prefix="Root: "):
    """
    Prints a binary tree horizontally.
    Right children appear on top, left children on the bottom.
    """
    if not root:
        return

    # Print right subtree first (top)
    if root.right:
        print_tree(root.right, level + 1, "┌── R: ")

    # Print current node
    print(" " * (level * 4) + prefix + str(root.val))

    # Print left subtree (bottom)
    if root.left:
        print_tree(root.left, level + 1, "└── L: ")

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
print(findMaximumPathSum(root))