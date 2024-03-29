import math
import time
from queue import PriorityQueue

blank_num = 0


def manhattan_distance_split(state, goal, remove_row_count, total_count, pre_count, zero_index_count):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            current = state[i][j]
            if current != blank_num:
                row, col = divmod(state[i][j] - 1, 9)
                row -= remove_row_count
                distance += abs(i - row) + abs(j - col)
            # elif current == blank_num:
            #     row, col = remove_row_count, 8
            #     distance += abs(i - row) + abs(j - col)
    return distance


# 计算曼哈顿距离
def manhattan_distance(state, goal, target_count, target_num, current_row, current_num_distance_rate):
    # current_row = 0
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            current_num = state[i][j]
            # if state[i][j] != blank_num and state[i][j] <= target_num:
            if state[i][j] != blank_num:
                row, col = divmod(state[i][j] - 1, 9)
                row -= current_row

                distance += abs(i - row) + abs(j - col)
                if current_num == target_num:
                    distance += current_num_distance_rate * (abs(i - row) + abs(j - col))
            # elif state[i][j] == blank_num:
            #     row, col = current_row, 8
            #     distance += abs(i - row) + abs(j - col)
    return distance


def manhattan_distance_target(state, goal, target_count, target_num, current_row, current_num_distance_rate):
    # current_row = 0
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            current_num = state[i][j]
            if state[i][j] != blank_num and state[i][j] <= target_num:
                row, col = divmod(state[i][j] - 1, 9)
                row -= current_row

                distance += abs(i - row) + abs(j - col)
                if current_num == target_num:
                    distance += current_num_distance_rate * (abs(i - row) + abs(j - col))
            # elif state[i][j] == blank_num:
            #     row, col = current_row, 8
            #     distance += abs(i - row) + abs(j - col)
    return distance


def manhattan_distance_bottom(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != blank_num:
                row, col = divmod(state[i][j] - 1, 9)
                row -= 6
                distance += abs(i - row) + abs(j - col)
    return distance


def a_star_split(ori_start, ori_goal, remove_row_count, total_count, pre_count, zero_index_count):
    start = ori_start[remove_row_count:]
    goal = ori_goal[remove_row_count:]
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 左、右、上、下
    frontier = PriorityQueue()
    frontier.put((blank_num, start, []))
    visited = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()

        flattened_current_state = [val for row in current_state for val in row]
        flattened_goal_state = [val for row in goal for val in row]

        if sorted(flattened_current_state[:total_count])[:pre_count + 1] == [0] + flattened_goal_state[
                                                                                  :pre_count] and 0 in flattened_current_state[
                                                                                                       :zero_index_count]:
            return path, current_state

        visited.add(tuple(map(tuple, current_state)))

        zero_row, zero_col = next(
            (i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == blank_num)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(start) and 0 <= new_col < 9:
                new_state = [row.copy() for row in current_state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], \
                    new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in visited:
                    distance = manhattan_distance_split(new_state, goal, remove_row_count, total_count, pre_count,
                                                        zero_index_count)
                    cost = len(path) + 1 + distance
                    frontier.put((cost, new_state, path + [(new_row, new_col)]))

    return None


# A*算法
def a_star(ori_start, ori_goal, row_index_start, row_index_end, target_count, target_num, current_row,
           current_num_distance_rate):
    start = ori_start[row_index_start:row_index_end]
    goal = ori_goal[row_index_start:row_index_end]

    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 左、右、上、下
    frontier = PriorityQueue()
    frontier.put((blank_num, start, []))
    visited = set()

    iterations = 0

    while not frontier.empty():
        iterations += 1
        if iterations > 100000:
            print("Exceeded maximum iterations. No solution found.")
            return [], [], False

        _, current_state, path = frontier.get()

        flattened_current_state = [val for row in current_state for val in row]
        flattened_goal = [val for row in goal for val in row]

        if flattened_current_state[:target_count] == flattened_goal[:target_count]:
            return path, current_state, True

        visited.add(tuple(map(tuple, current_state)))

        zero_row, zero_col = next(
            (i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == blank_num)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]
            last_row_num = current_row * 9

            if 0 <= new_row < len(start) and 0 <= new_col < 9 and current_state[new_row][new_col] > last_row_num:
                # if target_num >= target_count or new_col in [6, 7, 8]:
                if True:
                    new_state = [row.copy() for row in current_state]
                    new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], \
                        new_state[zero_row][zero_col]

                    if tuple(map(tuple, new_state)) not in visited:
                        if current_num_distance_rate == 0:
                            distance = manhattan_distance(new_state, goal, target_count, target_num, current_row,
                                                          current_num_distance_rate)
                        else:
                            distance = manhattan_distance_target(new_state, goal, target_count, target_num, current_row,
                                                                 current_num_distance_rate)
                        # cost = math.sqrt(len(path)) + 1 + distance
                        cost = len(path) + 1 + distance
                        frontier.put((cost, new_state, path + [(new_row, new_col)]))

    return None


def a_star_bottom(start, goal, target_count):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 左、右、上、下
    frontier = PriorityQueue()
    frontier.put((blank_num, start, []))
    visited = set()

    while not frontier.empty():
        _, current_state, path = frontier.get()

        # flattened_current_state = [val for row in current_state for val in row]
        # flattened_goal = [val for row in goal for val in row]

        flattened_current_state = [val for col in zip(*current_state) for val in col]
        flattened_goal = [val for col in zip(*goal) for val in col]

        if flattened_current_state[:target_count] == flattened_goal[:target_count]:
            return path, current_state

        visited.add(tuple(map(tuple, current_state)))

        zero_row, zero_col = next(
            (i, j) for i, row in enumerate(current_state) for j, val in enumerate(row) if val == blank_num)

        for move in moves:
            new_row, new_col = zero_row + move[0], zero_col + move[1]

            if 0 <= new_row < len(start) and 0 <= new_col < 9:
                new_state = [row.copy() for row in current_state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], \
                    new_state[zero_row][zero_col]

                if tuple(map(tuple, new_state)) not in visited:
                    distance = manhattan_distance_bottom(new_state, goal)
                    cost = len(path) + 1 + distance
                    frontier.put((cost, new_state, path + [(new_row, new_col)]))

    return None


# 打印棋盘状态
def print_board(state):
    for row in state:
        print(row)
    print()


def get_path(start, goal):
    print("start=")
    print(start)

    print("goal=")
    print(goal)

    start_time = time.time()

    step_indexs = []

    print("二分")
    path, current_state = a_star_split(start, goal, 0, 54, 27, 27)
    print("二分结束")
    if path:
        zero_row, zero_col = next(
            (i, j) for i, row in enumerate(start) for j, val in enumerate(row) if val == blank_num)

        for step, (row, col) in enumerate(path):
            start[row][col], start[zero_row][zero_col] = start[zero_row][zero_col], \
                start[row][col]
            zero_row, zero_col = row, col
            step_indexs.append((row, col))
    print(start)

    for deal_count in range(3):
        print("二分")
        # path, current_state = a_star_split(start, goal,0, 54, 27, 36)
        path, current_state = a_star_split(start, goal, deal_count * 2, 9 * 4, 9 * 2, 9 * 4)
        print("二分结束")
        if path:
            zero_row, zero_col = next(
                (i, j) for i, row in enumerate(start) for j, val in enumerate(row) if val == blank_num)

            for step, (row, col) in enumerate(path):
                row += deal_count * 2
                start[row][col], start[zero_row][zero_col] = start[zero_row][zero_col], \
                    start[row][col]
                zero_row, zero_col = row, col
                step_indexs.append((row, col))
        print(start)

        start_count = deal_count * 9 * 2
        # 执行A*算法
        for i in range(start_count, start_count + 9 * 2):
            print("start")
            print(i + 1)
            current_row = i // 9
            # path, current_state = a_star(start[current_row:], goal[current_row:], i + 1, current_row)
            path, current_state, star_result = a_star(start, goal, deal_count * 2, deal_count * 2 + 4,
                                                      i + 1 - start_count, i + 1,
                                                      current_row, 0)

            if not star_result:
                path, current_state, star_result = a_star(start, goal, deal_count * 2, deal_count * 2 + 4,
                                                          i + 1 - start_count, i + 1,
                                                          current_row, 10)

            if not star_result:
                return None

            if path:
                zero_row, zero_col = next(
                    (i, j) for i, row in enumerate(start) for j, val in enumerate(row) if val == blank_num)

                for step, (row, col) in enumerate(path):
                    row += deal_count * 2
                    start[row][col], start[zero_row][zero_col] = start[zero_row][zero_col], \
                        start[row][col]
                    zero_row, zero_col = row, col
                    step_indexs.append((row, col))
            print(start)

    print("已经拼好前n-2层")

    for i in range(27):
        print("start")
        print(i + 1)
        print(start)
        path, current_state = a_star_bottom(start[-3:], goal[-3:], i + 1)

        if path:
            current_state = [row.copy() for row in start]  # 初始化当前状态为初始状态
            zero_row, zero_col = next(
                (i, j) for i, row in enumerate(start) for j, val in enumerate(row) if val == blank_num)

            for step, (row, col) in enumerate(path):
                row += 6
                start[row][col], start[zero_row][zero_col] = start[zero_row][zero_col], \
                    start[row][col]
                zero_row, zero_col = row, col
                step_indexs.append((row, col))

    end_time = time.time()
    print(f"{end_time - start_time}秒")
    print(start)
    return step_indexs


def get_path_warp(start):
    numbers = [-1 if num == 99 else num for num in start]
    # 将数组中所有元素加1
    numbers = [num + 1 for num in numbers]
    # 将一维数组转换为二维数组
    numbers_2d = [numbers[i:i + 9] for i in range(0, len(numbers), 9)]

    split_count = 9
    given_array = list(range(1, split_count * split_count))
    given_array.append(0)
    # 将一维数组转换为二维数组
    given_array = [given_array[i:i + 9] for i in range(0, len(given_array), 9)]

    print("numbers_2d:")
    print(numbers_2d)
    print("goal:")
    print(given_array)

    paths = get_path(numbers_2d, given_array)
    indexs = []
    for path in paths:
        index = path[0] * 9 + path[1]
        indexs.append(index)
    return indexs

# start = [[1, 2, 3, 5, 14, 6, 7, 8, 9], [19, 10, 12, 4, 23, 26, 34, 17, 18], [11, 21, 29, 13, 25, 15, 16, 36, 35],
#          [40, 28, 22, 33, 31, 52, 24, 27, 44], [20, 30, 48, 47, 32, 42, 51, 60, 45],
#          [37, 46, 38, 39, 69, 62, 43, 78, 54], [55, 56, 75, 57, 50, 41, 67, 59, 63],
#          [64, 65, 76, 49, 68, 79, 58, 71, 80], [73, 74, 0, 66, 77, 70, 61, 53, 72]]
#
# # todo 求解困难 需要优化代码
# # [0, 1, 2, 13, 5, 15, 7, 25, 8, 27, 9, 11, 4, 3, 14, 99, 26, 16, 10, 18, 12, 19, 23, 21, 24, 32, 17, 28, 31, 30, 20, 22, 33, 34, 35, 6, 36, 47, 29, 39, 40, 41, 52, 43, 44, 46, 48, 37, 57, 49, 50, 42, 51, 53, 45, 63, 56, 58, 67, 59, 60, 61, 62, 73, 54, 38, 65, 66, 68, 78, 69, 71, 55, 64, 72, 74, 75, 76, 77, 70, 79]
# # start = [[1, 2, 3, 5, 15, 16, 17, 8, 9], [10, 12, 13, 4, 7, 23, 26, 6, 18], [19, 11, 21, 22, 14, 25, 60, 27, 36], [37, 30, 33, 20, 32, 24, 45, 43, 34], [49, 29, 28, 31, 41, 51, 42, 63, 54], [38, 65, 47, 39, 61, 69, 0, 52, 35], [46, 56, 48, 40, 50, 59, 70, 44, 62], [55, 64, 66, 57, 67, 78, 68, 72, 80], [73, 58, 74, 75, 76, 77, 53, 79, 71]]
# start = [[1, 2, 3, 4, 5, 6, 0, 16, 9], [10, 12, 13, 7, 23, 15, 17, 8, 18], [19, 11, 21, 22, 14, 25, 26, 27, 36],
#          [37, 30, 33, 20, 32, 24, 60, 43, 34], [49, 29, 28, 31, 41, 51, 45, 63, 54],
#          [38, 65, 47, 39, 61, 69, 42, 52, 35], [46, 56, 48, 40, 50, 59, 70, 44, 62],
#          [55, 64, 66, 57, 67, 78, 68, 72, 80], [73, 58, 74, 75, 76, 77, 53, 79, 71]]
#
# # # 目标状态
# goal = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27],
#         [28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45],
#         [46, 47, 48, 49, 50, 51, 52, 53, 54], [55, 56, 57, 58, 59, 60, 61, 62, 63],
#         [64, 65, 66, 67, 68, 69, 70, 71, 72], [73, 74, 75, 76, 77, 78, 79, 80, 0]]
# #
# # paths = get_path(start, goal)
# # print(paths)
#
# # numbers = [0, 1, 2, 4, 14, 15, 16, 7, 8, 9, 11, 12, 3, 6, 22, 25, 5, 17, 18, 10, 20, 21, 13, 24, 59, 26, 35, 36, 29, 32, 19, 31, 23, 44, 42, 33, 48, 28, 27, 30, 40, 50, 41, 62, 53, 37, 64, 46, 38, 60, 68, 99, 51, 34, 45, 55, 47, 39, 49, 58, 69, 43, 61, 54, 63, 65, 56, 66, 77, 67, 71, 79, 72, 57, 73, 74, 75, 76, 52, 78, 70]
# # path_warp = get_path_warp(numbers)
# # print(path_warp)
# # print("get_path_warp done")
#
# start = [[1, 4, 14, 8, 3, 2, 16, 15, 7], [10, 12, 27, 13, 33, 0, 36, 6, 9], [19, 28, 11, 20, 5, 22, 24, 18, 17], [37, 38, 31, 30, 23, 32, 26, 25, 35], [49, 46, 21, 40, 42, 51, 34, 44, 45], [47, 29, 48, 58, 50, 59, 43, 52, 54], [39, 73, 57, 67, 60, 41, 70, 53, 62], [56, 74, 66, 76, 68, 78, 69, 72, 63], [55, 64, 75, 65, 77, 79, 61, 71, 80]]
#
# goal = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27],
#         [28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45],
#         [46, 47, 48, 49, 50, 51, 52, 53, 54], [55, 56, 57, 58, 59, 60, 61, 62, 63],
#         [64, 65, 66, 67, 68, 69, 70, 71, 72], [73, 74, 75, 76, 77, 78, 79, 80, 0]]
# paths = get_path(start, goal)
# print(paths)
# print("get_path done")
