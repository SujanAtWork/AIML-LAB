#Write a python program to find the shortest path between srouce and destination on a graph using A* Search Algorithm.

import math
import heapq

#Define cell class 
def cell_class(self):
    self.parent_i = 0
    self.parent_j = 0
    self.f = float('inf')
    self.g = float('inf')
    self.h = 0 # Huerestic cost from this cell to destination

    
ROW = 5
COLUMN = 5

#check if cell is valid
def is_valid(row, col):
    return row > 0 and row < ROW and col > 0 and col < COLUMN

def is_unblocked(grid, row, col):
    return grid[row][col] = 1;

def is_destination(row, col, dest):
    return row = dest[0] and col = dest[1]

#define hueristic
D = 1 # lenght of each node
D2 = math.sqrt(2) # lenght of diagonal

def calculate_heuristic(row, col, dest):
    dx = abs(row - dest[0]) 
    dy = abs(col - dest[1])
    return (D * (dx + dy) + (D2 - 2 * D) * min(dx, dy))

#trace path
def trace_path(cell_details, dest):
    print('Path is')
    path = []
    row = dest[0]
    col = dest[1]

# trace back the path from destination to source
    while not((cell_details[row][col].parent_i == row) and (cell_details[row][col].parent_j == col)):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i 
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    #Add source cell to path
        path.append((row, col))

    #Reverse the path to get from source to destination
        path.reverse()

    #Print the path
        for i in path:
            print("->" , i , end=" ")
        print();


def A_star_algo(grid, src, dest):
    #check if src or dest is not valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is not valid")
        return

    #check if src or dest is unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or destination is blocked")
        return

    #check if we are already at destination
    if is_destination(grid, src[0], src[1]):
        print("We are already at destination")
        return

    #initialize closed list
    closed_list = [[False for _ in range(COLUMN)] for _ in range(ROW)]

    #Initialize details for each cell
    cell_details = [[Cell() for _ in range(COLUMN)] for _ in range(ROW)]

    #Initialize cell details for each cell
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    #initialize open list 
    open_list = []
    heapq.heappush(open_list, (0.0, i,j))

    # Initialize the flag for whether destination is found
    found_dest = False

    #Main loop for A_star algoritm
    while len(open_list) > 0:
        #pop the first element as p
        p = heapq.heappop(open_list)

        #mark the cell as visited in closed list
        i = p[0]
        j = p[1]
        closed_list[i][j] = True

        #for each directions check the successor
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1) (1,-1), (-1,1), (-1,-1)]
        for dir in directions:
            new_i = i + dir[0]
            new j = j + dir[1]

            #if successor is valid, unblocked and unvisited
            if is_valid(new_i, new_j) and is_unblocked(new_i, new_j) and not closed_list[new_i][new_j]:
                #if the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
