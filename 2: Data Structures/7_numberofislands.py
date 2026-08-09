from collections import deque

def count_islands(matrix):
    if not matrix:
        return 0
    total_islands = 0
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    def find_connecting(y, x):
        queue = deque([(y, x)])
        matrix[y][x] = 0
      
        while queue:
            current_y, current_x = queue.popleft()
            for yd, xd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_y = current_y + yd
                new_x = current_x + xd
                if 0 <= new_y < num_rows and 0 <= new_x < num_columns and matrix[new_y][new_x] == 1:
                    queue.append((new_y, new_x))
                    matrix[new_y][new_x] = 0
    
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 1:
                total_islands += 1
                find_connecting(y, x)

    return total_islands

"""
matrix = [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
for row in matrix:
    print(row)
print(str(count_islands(matrix)) + " Islands")
"""
