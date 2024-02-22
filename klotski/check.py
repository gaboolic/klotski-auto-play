from collections import deque
from itertools import permutations

# 定义初始状态和目标状态
start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
start_state = [1, 4, 8, 0, 7, 2, 5, 6, 3]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def is_solvable(puzzle):
    inversions = 0
    for i in range(len(puzzle) - 1):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0:
                inversions += 1

    blank_row = puzzle.index(0) // 3
    if (len(puzzle) % 2 == 1 and inversions % 2 == 0) or (
            len(puzzle) % 2 == 0 and (blank_row % 2 == 1) != (inversions % 2 == 0)):
        return True
    return False


# Check if a solution is possible between the start_state and goal state
if is_solvable(start_state) and is_solvable(goal_state):
    print("A solution is possible between the initial and goal states.")
else:
    print("No solution is possible between the initial and goal states.")
