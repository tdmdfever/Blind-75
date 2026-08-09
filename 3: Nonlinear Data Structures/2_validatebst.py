# Validate Binary Search Tree
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