"""
Given a binary tree, your task is to create two functions.

one for serializing the tree into a string format and another for deserializing 
the string back into the tree.

The serialized string should retain all the tree nodes and their connections, 
allowing for reconstruction without any loss of data.

Example 1:
Input: [1,2,3,null,null,4,5]
Expected Output: [1,2,3,null,null,4,5]
Justification: The tree has the structure:
  1
 / \
2   3
   / \
  4   5

When serialized and then deserialized, it should retain the exact 
same structure.

Example 2:
Input: [1,null,2,3]
Expected Output: [1,null,2,3]
Justification: The tree has the structure:
  1
   \
    2
   /
  3

When serialized and then deserialized, it should retain the exact same structure.

Example 3:
Input: [5,4,7,3,null,null,null,2]
Expected Output: [5,4,7,3,null,null,null,2]
Justification: The tree has the structure:
       5
     /   \
    4     7
   /     
  3    
 /
2
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode) -> str:
        if not root:
            return '[]'
        
        result = [str(root.val)]
        queue = deque([root.left, root.right])
        while queue:
            current_node = queue.popleft()
            if current_node:
                result.append(str(current_node.val))
                queue.extend([current_node.left, current_node.right])
            else:
                result.append('null')

        while result and result[-1] == 'null':
            result.pop()

        return '[' + ','.join(result) + ']'

def deserialize(data: str) -> TreeNode:
        if not data or data == '[]':
            return None
        
        datalist = data[1:len(data) - 1].split(',')
        root = TreeNode(int(datalist[0]))
        queue = deque([root])
        i = 0
        while queue:
            current_node = queue.popleft()
            i += 1
            if i < len(datalist) and datalist[i] != "null":
                left_node = TreeNode(int(datalist[i]))
                current_node.left = left_node
                queue.append(left_node)
            i += 1
            if i < len(datalist) and datalist[i] != "null":
                right_node = TreeNode(int(datalist[i]))
                current_node.right = right_node
                queue.append(right_node)            
                 
        return root

# Test
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

node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node1.left, node1.right = node2, node3
node3.left, node3.right = node4, node5

serialization = serialize(node1)
deserialization_root = deserialize(serialization)

print(serialization)
print_tree(deserialization_root)
print(serialize(deserialization_root))