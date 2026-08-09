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

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

print_tree(root)
print(is_valid_bst(root))