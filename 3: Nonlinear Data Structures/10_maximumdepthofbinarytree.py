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

def maxDepth(root):
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

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
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print_tree(root)
print(maxDepth(root))