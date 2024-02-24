import heapq


# 定义启发式函数，这里使用曼哈顿距离作为启发式函数
def heuristic(state):
    goal = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 0]]

    distance = 0
    for i in range(5):
        for j in range(5):
            if state[i][j] != 0:
                x_goal, y_goal = divmod(state[i][j] - 1, 5)
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
            if 0 <= x < 5 and 0 <= y < 5:
                new_state = [row.copy() for row in state]
                new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][
                    zero_pos[1]]

                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(heap, (g + heuristic(new_state), g + 1, new_state))

    return -1


# 初始状态
start = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 0, 23, 24]]

# 目标状态
goal = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 0]]

steps = astar(start)
if steps != -1:
    print("解决方案步数：", steps)
else:
    print("无解")
