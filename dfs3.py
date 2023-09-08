# Queue is a data structure that operates on a FIFO cycle(First In First Out)
from queue import Queue  


# copy has two methods to create copies
# deepcopy() is used to create a copy of the queue without any connection to the parent queue
# copy() is used to to create a copy of the queue with connection to the parent queue
import copy

# time is used to calculate the time spent solving the puzzle
import time


# function to display puzzle in the matrix format 
def display(p):
    global step # makes the step global.....to be used anywhere in the program
    for i in range(len(p)):
        if i %3 == 0 and i>0:
            print("")
        print(str(p[i])+" ",end="")
    print("\n")
    print("steps :",step)
    step += 1
    
# function to check the puzzle and also change the current node
def solve_puzzle(puzzle_state):
    global puzzle_index
    if puzzle_state==final_puzzle: # check if the current puzzle is equal to the final puzzle
        display(puzzle_state) # takes the puzzle to the function display and calls it
        return True # return true if they are equal
    if puzzle_state not in visitedList: # then we check if we have worked with that particular puzzle before so we don't end up in an endless loop
        display(puzzle_state)  # takes the puzzle to the function display and calls it
        queue.insert(puzzle_index, puzzle_state) # inserting the puzzle in a specific index
        visitedList.append(puzzle_state) # append puzzle to visitedlist so we don't repeat the same puzzle_state again
        puzzle_index +=1
    return False


initial_puzzle = [1,0,6, 3,4,5, 2,7,8]
final_puzzle = [0,1,2, 3,4,5, 6,7,8]

found = False
step = 0
visitedList = []
queue = []
queue.append(initial_puzzle) # moves the initial puzzle state into the queue
visitedList.append(initial_puzzle) # moves the initial puzzle state into the list 

t0 = time.time() # initial time or start  time

while (not found and not len(queue)==0): # check for if found is set to false and the queue is empty
    currentNode = queue.pop(0) # pop out the first value from the list
    empty_tile = currentNode.index(0) # set to the index value of 0 which stands for empty file
    puzzle_index = 0

    if empty_tile!=0 and empty_tile!=1 and empty_tile!=2: # check if the empty file is not on the first row of the puzzle
        State = copy.deepcopy(currentNode) # creates a copy of currentnode and is not connected to the currentnode
        State[empty_tile] = State[empty_tile-3] # set the location place of zero to another value 
        State[empty_tile-3] = 0 # set the location of another value to 0
        found = solve_puzzle(State) # call function solve_puzzle()
    if empty_tile!=0 and empty_tile!=3 and empty_tile!=6 and found==False: # checks if the empty_tile is not on the first column to move it to the left.
        State = copy.deepcopy(currentNode)
        State[empty_tile] = State[empty_tile-1]
        State[empty_tile-1] = 0
        found = solve_puzzle(State)
    if empty_tile!=6 and empty_tile!=7 and empty_tile!=8 and found==False: # checks if the empty_tile is not on the last row column to move it down.
        State = copy.deepcopy(currentNode)
        State[empty_tile] = State[empty_tile+3]
        State[empty_tile+3] = 0
        found = solve_puzzle(State)
    if empty_tile!=2 and empty_tile!=5 and empty_tile!=8 and found==False: # checks if the empty_tile is not on the last column to move it to the right.
        State = copy.deepcopy(currentNode)
        State[empty_tile] = State[empty_tile+1]
        State[empty_tile+1] = 0
        found = solve_puzzle(State)
t1 = time.time() # subtracts final time with initial time to get the time it takes to solve the puzzle
print('------')
print('Time:', t1-t0)

