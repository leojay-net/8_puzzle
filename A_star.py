from heapq import heappush as push, heappop as pop
import time

# function to return the Manhattan distance for a given puzzle state
def heuristics(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_i, target_j = (state[i][j] - 1) // 3, (state[i][j] - 1) % 3
                distance += abs(i - target_i) + abs(j - target_j)
    return distance

# function to check if a given puzzle state is the goal state
def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# function to return a list of possible next states for a given state...Move the empty tile through all possible direction and stores it in a list
def neighbours(state):
    nexts = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    next = [row[:] for row in state]
                    next[i][j], next[i-1][j] = next[i-1][j], next[i][j]
                    nexts.append(next)
                if i < 2:
                    next = [row[:] for row in state]
                    next[i][j], next[i+1][j] = next[i+1][j], next[i][j]
                    nexts.append(next)
                if j > 0:
                    next = [row[:] for row in state]
                    next[i][j], next[i][j-1] = next[i][j-1], next[i][j]
                    nexts.append(next)
                if j < 2:
                    next = [row[:] for row in state]
                    next[i][j], next[i][j+1] = next[i][j+1], next[i][j]
                    nexts.append(next)
    return nexts

# function to solve the 8 puzzle using A* search
def solve(state):
    if is_goal(state):
        return state
    heap = []
    push(heap, (heuristics(state), 0, state, [])) # push the values to the list heap
    visited = set() # a closed list of visited neighbours
    while heap:
        _, cost, state, puzzle_path = pop(heap) #pops values the list
        if is_goal(state):
            return puzzle_path
        if str(state) in visited:
            continue
        visited.add(str(state))
        for next in neighbours(state):
            push(heap, (heuristics(next) + cost + 1, cost + 1, next, puzzle_path + [next]))
    return None

# test the code with
t0 = time.time()
for i, puzzle in enumerate(solve([[1, 2, 5], [3, 4, 8], [6, 7, 0]])):
    for j in puzzle:
        print(j, "\n")
    print("steps :", i)
t1 = time.time()
print("time:",t1-t0)
