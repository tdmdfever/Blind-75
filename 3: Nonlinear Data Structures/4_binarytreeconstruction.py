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
