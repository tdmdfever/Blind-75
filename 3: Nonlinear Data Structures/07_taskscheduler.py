"""
There are 'N' tasks, labeled from '0' to 'N-1'. Each task can have some 
prerequisite tasks which need to be completed before it can be scheduled.

Given the number of tasks and a list of prerequisite pairs, find out if it is 
possible to schedule all the tasks.

Example 1:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 

Example 2:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. 
Similarly, task '1' needs to finish before '2' can be 
scheduled. One possible scheduling of tasks is: [0, 1, 2] 

Example 3:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have a cyclic dependency, therefore they 
cannot be scheduled.
"""

from collections import deque

class Solution:
    def is_scheduling_possible(self, tasks, prerequisites):
        sorted_order = []
        if tasks <= 0:
            return False

        degree = {i: 0 for i in range(tasks)}
        graph = {i: [] for i in range(tasks)}

        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            degree[child] += 1

        sources = deque()
        for key in degree:
            if degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            for child in graph[vertex]:
                degree[child] -= 1
                if degree[child] == 0:
                    sources.append(child)

        return len(sorted_order) == tasks

# Test:
sol = Solution()
print(sol.is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
print(sol.is_scheduling_possible(3, [[0, 1], [1, 2]]))
print(sol.is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
