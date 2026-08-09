"""
Given a binary search tree (BST) and two of its nodes, find the node that is 
the lowest common ancestor (LCA) of the two given nodes. The LCA of two 
nodes is the node that lies in between the two nodes in terms of value and 
is the furthest from the root. In other words, it's the deepest node where the 
two nodes diverge in the tree. Remember, in a BST, nodes have unique values.

Example 1:
Input:
BST: [6,2,8,0,4,7,9,null,null,3,5]
Node 1: 2
Node 2: 8
Expected Output: 6
Justification: The nodes 2 and 8 are on the left and right children of node 6. Hence, node 6 is their LCA.

Example 2:
Input:
BST: [6,2,8,0,4,7,9,null,null,3,5]
Node 1: 0
Node 2: 3
Expected Output: 2
Justification: The nodes 0 and 3 are on the left and right children of node 2, which is the closest ancestor to these nodes.

Example 3:
Input:
BST: [6,2,8,0,4,7,9,null,null,3,5]
Node 1: 4
Node 2: 5
Expected Output: 4
Justification: Node 5 is the right child of node 4. Hence, the LCA is node 4 itself.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    current = root
    lower, upper = min(p, q), max(p, q)

    while current:
        if upper < current.val:
            current = current.left
        elif lower > current.val:
            current = current.right
        else:
            return current

    return None

def lowestCommonAncesto_recur(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
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

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

print_tree(root)
print(lowestCommonAncestor(root, 2, 8).val)
print(lowestCommonAncestor(root, 0, 3).val)
print(lowestCommonAncestor(root, 4, 5).val) 