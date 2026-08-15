"""
Given the preorder and inorder traversal sequences of a binary tree, your 
task is to reconstruct this binary tree. Assume that the tree does not contain 
duplicate values.


Example 1:
Input:
Preorder: [1,2,4,5,3,6,7]
Inorder: [4,2,5,1,6,3,7]
Expected Output:
Tree Representation: [1,2,3,4,5,6,7]
Justification:
The first value in preorder (1) is the root. In the inorder list, everything 
left of value 1 is the left subtree and everything on the right is the 
right subtree. Following this pattern recursively helps in 
reconstructing the binary tree. All null value represents the leaf 
node.

Example 2:
Input:
Preorder: [8,5,9,7,1,12,2,4,11,3]
Inorder: [9,5,1,7,2,12,8,4,3,11]
Expected Output:
Tree Representation: [8,5,4,9,7,11,1,12,2,null,3]
Justification:
Start with 8 (from preorder) as the root. Splitting at 8 in inorder, we 
find the left and right subtrees. Following this pattern recursively, we 
can construct the tree.

Example 3:
Input:
Preorder: [3,5,6,2,7,4,1,9,8]
Inorder: [6,5,7,2,4,3,9,1,8]
Expected Output:
Tree Representation: [3,5,1,6,2,9,8,null,null,7,4]
Justification:
Following the same approach, using 3 as root from preorder, we split 
the inorder sequence into left and right subtrees and continue 
recursively.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  # Constructor for the TreeNode class

# Construct Binary Tree from Preorder and Inorder Traversal
def build_tree(preorder, inorder):
    if not preorder:
        return None
    
    root = TreeNode(preorder[0])
    for i in range(len(inorder)):
        if inorder[i] == preorder[0]:
            index = i

    left = inorder[:index]
    right = inorder[index + 1:]

    root.left = build_tree(preorder[1:1 + len(left)], left)
    root.right = build_tree(preorder[1 + len(left):], right)

    return root

# Test:
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_utils import print_tree

root = build_tree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])

print_tree(root)