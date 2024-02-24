import math
from queue import Queue

# 定义初始状态和目标状态
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
    print(goal_state)
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

numbers = [12, 23, 10, 9, 4, 17, 21, 8, 5, 1, 22, 6, 0, 14, 11, 7, 15, 13, 3, 18, 2, 19, 99, 20, 16]
goal_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 99]
steps = get_path(numbers)
print(steps)