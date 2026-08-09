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

node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node1.left, node1.right = node2, node3
node3.left, node3.right = node4, node5

serialization = serialize(node1)

print(serialization)
print(serialize(deserialize(serialization)))