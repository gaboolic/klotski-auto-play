from queue import PriorityQueue

# 计算曼哈顿距离
def manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 5)
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

            if 0 <= new_row < 5 and 0 <= new_col < 5:
                new_state = [row.copy() for row in current_state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in visited:
                    cost = len(path) + 1 + manhattan_distance(new_state, goal)
                    frontier.put((cost, new_state, path + [(new_row, new_col)]))

    return None

# 打印棋盘状态
def print_board(state):
    for row in state:
        print(row)
    print()

start = [
    [7,22,5,15,8],
    [1,12,13,6,9],
    [4,18,21,8,20],
    [0,2,11,23,19],
    [3,24,16,14,17]
]




# 目标状态
goal = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,0]
]
# path, current_state = a_star(start, goal, 2)
# print(path)
# print(current_state)


# 执行A*算法
for i in range(15):
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

