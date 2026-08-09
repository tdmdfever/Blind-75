import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMaximumPathSum(root):
    globalMaximumSum = -math.inf
    
    def maximumPathSumAt(node):
        nonlocal globalMaximumSum
        if not node:
            return 0

        left_gain = max(maximumPathSumAt(node.left), 0)
        right_gain = max(maximumPathSumAt(node.right), 0)

        globalMaximumSum = max(globalMaximumSum, node.val + left_gain + right_gain)

        return node.val + max(left_gain, right_gain)

    maximumPathSumAt(root)
    return globalMaximumSum