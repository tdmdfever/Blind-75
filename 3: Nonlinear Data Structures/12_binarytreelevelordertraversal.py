from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(root):
    result = []
    queue = deque([(0, root)])
    while queue:
        (level, node) = queue.popleft()
        if node:
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)
                queue.extend([(level + 1, node.left), (level + 1, node.right)])

    return result