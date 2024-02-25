from queue import PriorityQueue

# 计算曼哈顿距离
def manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 3)
                distance += abs(i - row) + abs(j - col)
    return distance

# A*算法
def a_star(start, goal):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 左、右、上、下
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    visited = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()

        if current_state == goal:
            return path

        visited.add(tuple(map(tuple, current_state)))

        zero_row, zero_col = next((i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == 0)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
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

# 初始状态
start = [[8, 3, 5],
        [6, 7, 2],
        [4, 1, 0]]

# 目标状态
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# 执行A*算法
# 执行A*算法
path = a_star(start, goal)

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
        print_board(current_state)
        zero_row, zero_col = row, col

else:
    print("无法找到解决方案。")

