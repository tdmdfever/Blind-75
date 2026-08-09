from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(s, t):
        def isSameTree(p, q):
            if not p and not q:
                return True
            if (p and q and p.val == q.val):
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False
        
        queue = deque([s])
        while queue:
            node = queue.popleft()
            if node:
                queue.extend([node.left, node.right])
                if node.val == t.val and isSameTree(node, t):
                    return True
        return False