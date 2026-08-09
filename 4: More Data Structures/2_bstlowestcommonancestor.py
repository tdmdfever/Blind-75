class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    current_node = root
    lower, upper = min(p, q), max(p, q)
    while current_node.left or current_node.right:


        left = current_node.left.val
        right = current_node.right.val
        if lower < left < right < upper:
            return current_node.val
        elif lower < left < upper:
            current_node = current_node.left
        elif lower < right < upper:
            current_node = current_node.right
        elif left in (lower, upper) or right in (lower, upper):
            return current_node.val

        
    return None

