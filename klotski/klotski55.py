import heapq
import math


# 定义启发式函数，这里使用曼哈顿距离作为启发式函数
# def heuristic(state):
#     distance = 0
#     for i in range(5):
#         for j in range(5):
#             if state[i][j] != 0:
#                 x_goal, y_goal = divmod(state[i][j] - 1, 5)
#                 distance += abs(x_goal - i) + abs(y_goal - j)
#
#     return distance

def heuristic(state,goal):
    distance = 0
    for i in range(5):
        for j in range(5):
            if state[i][j] != goal[i][j]:
                distance = 25-(i+1)*(j+1)
                break

    return distance

# A*算法
# A*算法
def astar(start):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = [(heuristic(start,goal), 0, start)]
    visited = set()
    optimal_cost = float('inf')  # 初始化最优代价为无穷大

    while heap:
        f, g, state = heapq.heappop(heap)

        if g + heuristic(state,goal) >= optimal_cost:  # 如果当前节点的估计代价大于等于已知最优解，剪枝
            continue

        if state == goal:
            optimal_cost = g
            continue

        visited.add(tuple(map(tuple, state)))

        zero_pos = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

        for dx, dy in moves:
            x, y = zero_pos[0] + dx, zero_pos[1] + dy
            if 0 <= x < 5 and 0 <= y < 5:
                new_state = [row.copy() for row in state]
                new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = new_state[x][y], new_state[zero_pos[0]][zero_pos[1]]

                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(heap, (g + heuristic(new_state,goal), g + 1, new_state))

    return optimal_cost



# 初始状态
start = [[7, 22, 5, 15, 8],
         [1, 12, 13, 6, 9],
         [4, 18, 21, 10, 14],
         [0, 2, 11, 23, 19],
         [3, 24, 16, 14, 17]]


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
