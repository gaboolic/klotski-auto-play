import heapq


# 定义启发式函数，这里使用曼哈顿距离作为启发式函数
def heuristic(state,goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                distance = 81-(i+1)*(j+1)
                break

    return distance


# A*算法
def astar(start):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(heuristic(start,goal), 0, start)]
    visited = set()

    while heap:
        f, g, state = heapq.heappop(heap)

        if state == goal:
            return g

        visited.add(tuple(map(tuple, state)))

        zero_pos = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

        for dx, dy in moves:
            x, y = zero_pos[0] + dx, zero_pos[1] + dy
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = [row.copy() for row in state]
                new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][
                    zero_pos[1]]

                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(heap, (g + heuristic(new_state,goal), g + 1, new_state))

    return -1


# 初始状态
start = [[8, 3, 5],
        [6,7,2],
        [4,1,0]]


# 目标状态
goal = [[1, 2, 3],
        [4,5,6],
        [7,8,0]]

steps = astar(start)
if steps != -1:
    print("解决方案步数：", steps)
else:
    print("无解")
