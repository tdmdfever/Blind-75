"""
Given a reference of a node in a connected undirected graph, return a deep 
copy (clone) of the graph. Each node in the graph contains a value (int) and 
a list (List[Node]) of its neighbors.

Example 1:
Input:

    1--2
    |  |
    4--3
Expected Output:

    1--2
    |  |
    4--3

Explanation: The graph has four nodes with the following connections:
Node 1 is connected to nodes 2 and 4.
Node 2 is connected to nodes 1 and 3.
Node 3 is connected to nodes 2 and 4.
Node 4 is connected to nodes 1 and 3.

Example 2:
Input:

    1--2
   /    \
  5      3
         |
         4
Expected Output:

    1--2
   /    \
  5      3
         |
         4

Explanation: The graph consists of five nodes with these connections:
Node 1 is connected to nodes 2 and 5.
Node 2 is connected to nodes 1 and 3.
Node 3 is connected to nodes 2 and 4.
Node 4 is connected to node 3.
Node 5 is connected to node 1.

Example 3:
Input:

    1--2
   /    \
  4      3
   \    /
    5--6
Expected Output:

    1--2
   /    \
  4      3
   \    /
    5--6
    
Explanation: The graph has six nodes with the following connections:
Node 1 is connected to nodes 2 and 4.
Node 2 is connected to nodes 1 and 3.
Node 3 is connected to nodes 2 and 6.
Node 4 is connected to nodes 1 and 5.
Node 5 is connected to nodes 4 and 6.
Node 6 is connected to nodes 3 and 5.
"""

from collections import deque

class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'GraphNode') -> 'GraphNode':
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

# Test:
node1 = GraphNode(1)
node2 = GraphNode(2)

node1.neighbors.append(node2)
node2.neighbors.append(node1)

new_node1 = clone_graph(node1)
print(new_node1.val)

for neighbor in new_node1.neighbors:
    print(str(neighbor.val) + ": " + str(len(neighbor.neighbors)) + ": " + str(neighbor.neighbors[0].val))
