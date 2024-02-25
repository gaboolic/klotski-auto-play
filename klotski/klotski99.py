import time
from queue import PriorityQueue

# 计算曼哈顿距离
def manhattan_distance(state, goal, target_count):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 9)
                distance += abs(i - row) + abs(j - col)
    return distance

def manhattan_distance_bottom(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 9)
                row -= 7
                distance += abs(i - row) + abs(j - col)
    return distance

# A*算法
def a_star(start, goal, target_count):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 左、右、上、下
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    visited = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()

        flattened_current_state = [val for row in current_state for val in row]
        flattened_goal = [val for row in goal for val in row]

        if flattened_current_state[:target_count] == flattened_goal[:target_count]:
            return path, current_state

        visited.add(tuple(map(tuple, current_state)))

        zero_row, zero_col = next((i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == 0)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(start) and 0 <= new_col < 9:
                new_state = [row.copy() for row in current_state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in visited:
                    distance = manhattan_distance(new_state,goal,target_count)
                    cost = len(path) + 1 + distance
                    frontier.put((cost, new_state, path + [(new_row, new_col)]))

    return None

def a_star_bottom(start, goal, target_count):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 左、右、上、下
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    visited = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()

        flattened_current_state = [val for row in current_state for val in row]
        flattened_goal = [val for row in goal for val in row]

        if flattened_current_state[:target_count] == flattened_goal[:target_count]:
            return path, current_state

        visited.add(tuple(map(tuple, current_state)))

        zero_row, zero_col = next((i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == 0)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(start) and 0 <= new_col < 9:
                new_state = [row.copy() for row in current_state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in visited:
                    distance = 0
                    if len(start) == 9:
                        distance = manhattan_distance(new_state,goal,target_count)
                    else:
                        distance = manhattan_distance_bottom(new_state,goal)
                    cost = len(path) + 1 + distance
                    frontier.put((cost, new_state, path + [(new_row, new_col)]))

    return None

# 打印棋盘状态
def print_board(state):
    for row in state:
        print(row)
    print()

start_time = time.time()
start = [[1, 2, 3, 5, 14, 6, 7, 8, 9], [19, 10, 12, 4, 23, 26, 34, 17, 18], [11, 21, 29, 13, 25, 15, 16, 36, 35], [40, 28, 22, 33, 31, 52, 24, 27, 44], [20, 30, 48, 47, 32, 42, 51, 60, 45], [37, 46, 38, 39, 69, 62, 43, 78, 54], [55, 56, 75, 57, 50, 41, 67, 59, 63], [64, 65, 76, 49, 68, 79, 58, 71, 80], [73, 74, 0, 66, 77, 70, 61, 53, 72]]

# 目标状态
goal = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45], [46, 47, 48, 49, 50, 51, 52, 53, 54], [55, 56, 57, 58, 59, 60, 61, 62, 63], [64, 65, 66, 67, 68, 69, 70, 71, 72], [73, 74, 75, 76, 77, 78, 79, 80, 0]]

path, current_state = a_star(start, goal, 2)
print(path)
print(current_state)


# 执行A*算法
for i in range(63):
    print("start")
    print(i+1)
    print(start)
    path, current_state = a_star(start, goal, i+1)

    if path:
        current_state = [row.copy() for row in start]  # 初始化当前状态为初始状态
        zero_row, zero_col = next((i, j) for i, row in enumerate(start) for j, val in enumerate(row) if val == 0)

        print("初始状态：")
        print_board(current_state)

        print("移动步骤：")
        for step, (row, col) in enumerate(path):
            current_state[row][col], current_state[zero_row][zero_col] = current_state[zero_row][zero_col], \
            current_state[row][col]
            print(f"Step {step + 1}: Move 0 to ({row}, {col})")
            print(current_state)
            zero_row, zero_col = row, col

    else:
        print("无须操作")

    start = current_state

print("已经拼好前n-2层")

start = start[-2:]
print("start")
print(start)

for i in range(18):
    print("start")
    print(i+1)
    print(start)
    path, current_state = a_star_bottom(start[-2:], goal[-2:], i+1)

    if path:
        current_state = [row.copy() for row in start]  # 初始化当前状态为初始状态
        zero_row, zero_col = next((i, j) for i, row in enumerate(start) for j, val in enumerate(row) if val == 0)

        print("初始状态：")
        print_board(current_state)

        print("移动步骤：")
        for step, (row, col) in enumerate(path):
            current_state[row][col], current_state[zero_row][zero_col] = current_state[zero_row][zero_col], \
            current_state[row][col]
            print(f"Step {step + 1}: Move 0 to ({row}, {col})")
            print(current_state)
            zero_row, zero_col = row, col

    else:
        print("无须操作")

    start = current_state
end_time = time.time()
print(f"{end_time-start_time}秒")


