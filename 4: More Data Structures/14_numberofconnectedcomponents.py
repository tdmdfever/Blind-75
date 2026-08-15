"""
Given an undirected graph represented by 'n' nodes labeled from 0 to n-1 
and a list of undirected edges (each edge is a pair of nodes), determine the 
number of connected components in the graph. A connected component is a 
group of nodes that are directly or indirectly linked to each other through the edges.
"""

class Solution:
    def __init__(self):
        self.parents = []

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def count_components(self, n, edges):
        self.parents = [i for i in range(n)]
        for edge in edges:
            root1 = self.find(edge[0])
            root2 = self.find(edge[1])
            if root1 != root2:
                self.parents[root1] = root2
                n -= 1 
        return n
    
# Test:
sol = Solution()
print(sol.count_components(4, [[0,1],[2,3]]))
print(sol.count_components(5, [[0,1],[1,2],[2,0]]))
print(sol.count_components(3, []))