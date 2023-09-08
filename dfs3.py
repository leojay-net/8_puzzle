import copy
import time

def neighbours(p_state):
    nexts = []
    empty_tile = p_state.index(0)
    currentNode = p_state
    if empty_tile!=0 and empty_tile!=1 and empty_tile!=2: # check if the empty file is not on the first row of the puzzle
        State = copy.deepcopy(currentNode) # creates a copy of currentnode and is not connected to the currentnode
        State[empty_tile] = State[empty_tile-3] # set the location place of zero to another value 
        State[empty_tile-3] = 0 # set the location of another value to 0
        nexts.append(State)
    if empty_tile!=0 and empty_tile!=3 and empty_tile!=6: # checks if the empty_tile is not on the first column to move it to the left.
        State = copy.deepcopy(currentNode)
        State[empty_tile] = State[empty_tile-1]
        State[empty_tile-1] = 0
        nexts.append(State)
    if empty_tile!=6 and empty_tile!=7 and empty_tile!=8: # checks if the empty_tile is not on the last row column to move it down.
        State = copy.deepcopy(currentNode)
        State[empty_tile] = State[empty_tile+3]
        State[empty_tile+3] = 0
        nexts.append(State)
    if empty_tile!=2 and empty_tile!=5 and empty_tile!=8: # checks if the empty_tile is not on the last column to move it to the right.
        State = copy.deepcopy(currentNode)
        State[empty_tile] = State[empty_tile+1]
        State[empty_tile+1] = 0
        nexts.append(State)
    return nexts

def is_goal_state(state):

    return state == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def solve_8puzzle(initial_board):
  # Create a stack to store the board configurations that we need to visit
  global step
  step = 0
  stack = []
  # Push the initial board configuration onto the stack
  stack.append(initial_board)
  # Create a set to store the board configurations that we have already visited
  #print("stack=",stack)
  visited_boards = set()
  # While the stack is not empty
  while not len(stack) == 0:
    # Pop the top board configuration from the stack
    board = stack.pop()
    # If the board is the goal state, return it
    if is_goal_state(board):
      return display(board)
    #print(1)
    # Otherwise, add the board to the set of visited board configurations
    visited_boards.add(tuple(board))
    #print("visited = ",visited_boards)
    # Generate the list of possible next board configurations
    next_boards = neighbours(board)
    # For each possible next board configuration
    for next_board in next_boards:
      # If the board has not been visited
      if tuple(next_board) not in visited_boards:
        # Push it onto the stack
        stack.append(next_board)
    
  # If we have exhausted the stack and not found the goal state, return None
  return None
def display(p):
    global step # makes the step global.....to be used anywhere in the program
    for i in range(len(p)):
        if i %3 == 0 and i>0:
            print("")
        print(str(p[i])+" ",end="")
    print("\n")
    #print("steps :",step)
    step += 1

t0 = time.time()
print(solve_8puzzle([1, 2, 5, 3, 4, 8, 6, 7, 0]))
t1 = time.time()
print("time=", t1-t0)
