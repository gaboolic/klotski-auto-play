import math
from queue import Queue

# 定义初始状态和目标状态
# start_state = [0, 1, 2, 4, 13, 5, 6, 7, 8, 18, 9, 11, 3, 22, 25, 33, 16, 17, 10, 20, 28, 12, 24, 14, 15, 35, 34, 39, 27, 21, 32, 30, 51, 23, 26, 43, 19, 29, 47, 46, 31, 41, 50, 59, 44, 36, 45, 37, 38, 68, 61, 42, 77, 53, 54, 55, 74, 56, 49, 40, 66, 58, 62, 63, 64, 75, 48, 67, 78, 57, 70, 79, 72, 73, 99, 65, 76, 69, 60, 52, 71]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 99]


def print_puzzle(state):
    total = len(state)
    length = int(math.sqrt(total))
    for i in range(0, total, length):
        print(state[i:i + length])

def move(state, from_i, to_i):
    state_copy = state.copy()
    state_copy[to_i], state_copy[from_i] = state_copy[from_i], state_copy[to_i]
    return state_copy

def bfs(start_state, goal_state):
    visited = set()
    queue = Queue()
    queue.put((start_state, []))

    while not queue.empty():
        current_state, path = queue.get()

        if current_state == goal_state:
            return path

        zero_index = current_state.index(99)

        total = len(start_state)
        length = int(math.sqrt(total))

        for move_to in [1, -1, length, -length]:
            new_index = zero_index + move_to

            if 0 <= new_index < total and (zero_index % length != 0 or move_to != -1) and (zero_index % length != (length-1) or move_to != 1):
                new_state = move(current_state, zero_index, new_index)

                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    new_path = path.copy()
                    new_path.append((zero_index, new_index))
                    queue.put((new_state, new_path))

    return None

def get_path(start_state):
    goal_state = sorted(start_state)
    path = bfs(start_state, goal_state)

    swaps = []
    if path:
        for i, swap in enumerate(path):
            swaps.append(swap)
        return swaps

    else:
        return []


def show_path(start_state, goal_state):
    path = bfs(start_state, goal_state)

    if path:
        current_state = start_state
        print("Initial state:")
        print_puzzle(start_state)

        for i, swap in enumerate(path):
            from_i, to_i = swap
            current_state = move(current_state, from_i, to_i)

            print("\nStep", i + 1)
            print_puzzle(current_state)
            print("Swapped indexes:", swap)

    else:
        print("No solution found.")