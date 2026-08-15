"""
You are given a matrix grid of size m x n, where each matrix[i][j] 
represents the height of the Island at ith row and jth column position from 
the sea level. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

Due to heavy rain, there is a lot of water on each cell of the island. It is given 
that the rain water can flow to neighboring cells directly north, south, 
east, and west if the neighboring cell's height is less than or equal to 
the current cell's height. Water can flow from any cell adjacent to an ocean 
into the ocean.

Return a 2D list result, where result[i] = [ri, ci] represents that rainwater 
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:

Input: matrix =
[[1,2,2,3],
 [3,2,3,4],
 [2,4,5,3],
 [5,7,1,4]]
Expected Output: [[0, 3], [1, 3], [2, 2], [3, 0], [3, 1]]
Image
Justification: The cells that can flow to both the Pacific and Atlantic oceans are [[0, 3], [1, 3], [2, 2], [3, 0], [3, 1]]
[0,3]:
[0, 3] -> Pacific Ocean.
[0, 3] -> Atlantic Ocean.
[1,3]:
[1, 3] -> [0, 3] -> Pacific Ocean.
[1, 3] -> Atlantic Ocean.
[2, 2]:
[2, 2] -> [1, 2] -> [0, 2] -> Pacific Ocean.
[2, 2] -> [2, 3] -> Atlantic Ocean.
[3,0]:
[3, 0] -> Pacific Ocean.
[3, 0] -> Atlantic Ocean.
[3,1]:
[3, 1] -> [3, 0] -> Pacific Ocean.
[3, 1] -> Atlantic Ocean.

Example 2:
Input: matrix =
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Expected Output: [[0,2],[1,2],[2,0],[2,1],[2,2]]
Image
Justification: The cells that can flow to both the Pacific and Atlantic oceans are
[0,2]:
[0, 2] -> Pacific Ocean.
[0, 2] -> Atlantic Ocean.
[1,2]:
[1,2] -> [0,2] -> Pacific Ocean.
[1,2] -> Atlantic Ocean.
[2,0]:
[2, 0] -> Pacific Ocean.
[2, 0] -> Atlantic Ocean.
[2,1]:
[2,1] -> [1,1] -> [1, 0] -> Pacific Ocean.
[2,1] -> Atlantic Ocean.
[2,2]:
[2, 2] -> Pacific Ocean.
[2, 2] -> Atlantic Ocean.

Example 3:
Input: matrix =
[[10,10,10],
 [10,1,10],
 [10,10,10]]
Expected Output: [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
Image
Justification: The water can flow to both oceans from all cells except from the central cell [1,1].
"""

from collections import deque

def pacific_atlantic(matrix):
    def search(starts):
        queue = deque(starts)
        reachable = set(queue)

        while queue:
            current_y, current_x = queue.popleft()

            for yd, xd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_y, new_x = current_y + yd, current_x + xd

                if (0 <= new_y < len(matrix) and
                    0 <= new_x < len(matrix[0]) and
                    matrix[new_y][new_x] >= matrix[current_y][current_x] and
                    (new_y, new_x) not in reachable):

                    queue.append((new_y,new_x))
                    reachable.add((new_y,new_x))

        return reachable

    pacific_top = [(0,x) for x in range(len(matrix[0]))]
    pacific_left = [(y,0) for y in range(1, len(matrix))]
    atlantic_bottom = [(len(matrix) - 1,x) for x in range(len(matrix[len(matrix) - 1]))]
    atlantic_right = [(y,len(matrix[len(matrix) - 1]) - 1) for y in range(len(matrix) - 1)]

    return search(pacific_top + pacific_left) & search(atlantic_bottom + atlantic_right)

# Test:
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(pacific_atlantic(matrix1))
matrix2 = [
    [1,2,2,3],
    [3,2,3,4],
    [2,4,5,3],
    [5,7,1,4]
]
print(pacific_atlantic(matrix2))
