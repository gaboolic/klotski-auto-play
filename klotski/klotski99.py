import heapq


# 定义启发式函数，这里使用曼哈顿距离作为启发式函数
def heuristic(state):
    distance = 0
    for i in range(9):
        for j in range(9):
            if state[i][j] != 0:
                x_goal, y_goal = divmod(state[i][j] - 1, 9)
                distance += abs(x_goal - i) + abs(y_goal - j)

    return distance


# A*算法
def astar(start):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(heuristic(start), 0, start)]
    visited = set()

    while heap:
        f, g, state = heapq.heappop(heap)

        if state == goal:
            return g

        visited.add(tuple(map(tuple, state)))

        zero_pos = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

        for dx, dy in moves:
            x, y = zero_pos[0] + dx, zero_pos[1] + dy
            if 0 <= x < 9 and 0 <= y < 9:
                new_state = [row.copy() for row in state]
                new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][
                    zero_pos[1]]

                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(heap, (g + heuristic(new_state), g + 1, new_state))

    return -1


# 初始状态
start = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27],
        [28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50, 51, 52, 53, 54], [55, 56, 57, 58, 59, 60, 61, 62, 63],
        [64, 65, 66, 67, 68, 69, 0, 70, 71],
        [73, 74, 75, 76, 77, 78, 79, 80, 72]]
# start = [[1, 2, 3, 5, 14, 6, 7, 8, 9], [19, 10, 12, 4, 23, 26, 34, 17, 18], [11, 21, 29, 13, 25, 15, 16, 36, 35],
#          [40, 28, 22, 33, 31, 52, 24, 27, 44], [20, 30, 48, 47, 32, 42, 51, 60, 45],
#          [37, 46, 38, 39, 69, 62, 43, 78, 54], [55, 56, 75, 57, 50, 41, 67, 59, 63],
#          [64, 65, 76, 49, 68, 79, 58, 71, 80], [73, 74, 0, 66, 77, 70, 61, 53, 72]]

# 目标状态
goal = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27],
        [28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50, 51, 52, 53, 54], [55, 56, 57, 58, 59, 60, 61, 62, 63],
        [64, 65, 66, 67, 68, 69, 70, 71, 72], [73, 74, 75, 76, 77, 78, 79, 80, 0]]

steps = astar(start)
if steps != -1:
    print("解决方案步数：", steps)
else:
    print("无解")
