"""
Given the root of a binary tree, invert it.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS:
def invert_tree_bfs(root):
    if not root:
        return None

    queue = deque([root])

    while queue:
        current = queue.popleft()

        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return root

# DFS Iterative

def invert_tree_dfs_iterative(root):
    if not root:
        return None
    
    stack = [root]

    while stack:
        current = stack.pop()

        current.left, current.right = current.right, current.left
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return root 

# DFS Recursive
def invert_tree_dfs_recursive(root):
    if not root:
        return None

    root.left, root.right - invert_tree_dfs_recursive(root.right), invert_tree_dfs_recursive(root.left)

    return root

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

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.right.left = TreeNode(14)
root.right.right = TreeNode(19)
root.right.right.right = TreeNode(20)

print_tree(invert_tree_bfs(root))