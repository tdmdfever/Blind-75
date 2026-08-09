from collections import deque

# Invert Binary Tree

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