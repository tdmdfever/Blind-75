from collections import deque

# Clone Graph

class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: 'GraphNode') -> 'GraphNode':
    clone_node = GraphNode(node.val, [])
    reference_queue = deque([node])
    clone_dict = {node: clone_node}
    added = set(reference_queue)

    while reference_queue:
        current_reference_node = reference_queue.popleft()
        current_clone_node = clone_dict[current_reference_node]
        for neighbor in current_reference_node.neighbors:
            if neighbor not in added:
                clone_neighbor = GraphNode(neighbor.val, [current_clone_node])
                current_clone_node.neighbors.append(clone_neighbor)
                reference_queue.append(neighbor)
                added.add(neighbor)
                clone_dict[neighbor] = clone_neighbor
            elif current_clone_node not in clone_dict[neighbor].neighbors:
                current_clone_node.neighbors.append(clone_dict[neighbor])
                clone_dict[neighbor].neighbors.append(current_clone_node)
                    
                    

    return clone_node

"""
node1 = GraphNode(1)
node2 = GraphNode(2)

node1.neighbors.append(node2)
node2.neighbors.append(node1)

new_node1 = cloneGraph(node1)
print(new_node1.val)

for neighbor in new_node1.neighbors:
    print(str(neighbor.val) + ": " + str(len(neighbor.neighbors)) + ": " + str(neighbor.neighbors[0].val))
"""

