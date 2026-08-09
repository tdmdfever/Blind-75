from collections import deque

# 10. Pacific Atlantic Water Flow

def pacific_atlantic(matrix):
    def search(starts):
        queue = deque(starts)
        possible = set(queue)

        while queue:
            current_y, current_x = queue.popleft()

            for yd, xd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_y, new_x = current_y + yd, current_x + xd

                if (0 <= new_y < len(matrix) and 
                    0 <= new_x < len(matrix[0]) and
                    matrix[new_y][new_x] >= matrix[current_y][current_x] and 
                    (new_y, new_x) not in possible):

                    queue.append((new_y,new_x))
                    possible.add((new_y,new_x))

        return possible

    pacific_top = [(0,x) for x in range(len(matrix[0]))]
    pacific_left = [(y,0) for y in range(1, len(matrix))]
    atlantic_right = [(len(matrix) - 1,x) for x in range(len(matrix[len(matrix) - 1]))]
    atlantic_bottom = [(y,len(matrix[len(matrix) - 1]) - 1) for y in range(len(matrix) - 1)]

    return search(pacific_top + pacific_left) & search(atlantic_right + atlantic_bottom)

"""
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
"""