#create a counter
#use nested loops, by length of the grid
# if the element = s, check if it is a start of a ship or just a single S

# if i is 0, which means we are at the most left of the grid, 
# OR the element of the left of the S is = '.' 
# AND
# if j is 0, which means we are at the most left of the grid, OR element below S is '.'
# if true, increase count by 1

# return count
# create a variable for # rows
# create a variable for the len column - 1st one, if the rows >0
# use nested loops for 0


def count_uneven_grid_ships(grid):
    count = 0
    
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            
            current_cell = grid[row][column]
            
            if current_cell == 'S':
                cell_to_left = grid[row][column-1]
                
                try:
                    cell_above = grid[row-1][column]
                except IndexError:
                    pass  
                
                if (row == 0 or cell_above == '.') and (column == 0 or cell_to_left == '.'):
                    count +=1
              
    return count


let_ships = [
    [".", "S", ".", "S"],
    [".", ".", ".", "S"],
    ["S", "S", ".", "S"],
    [".", ".", ".", "S"]
]

let_ships2 = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"]
]

let_ships3 = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"],
    [".", ".", ".", "S", "S", "S", ".", "."],
    ["S", ".", ".", "S", "S", "S", ".", "."],
    ["S", ".", ".", ".", ".", ".", "S", "S"]
]

let_ships4 = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", ".",'.'],
    ["S", "S", ".", ".", ".", ".", "S", "S",'.','S'],
    [".", ".", ".", "S", "S", "S", ".", "."],
    ["S", ".", ".", "S", "S", "S", ".", "."],
    ["S", ".", ".", ".", ".", ".", "S", "S"]
]

print(count_uneven_grid_ships(let_ships))
print(count_uneven_grid_ships(let_ships2))
print(count_uneven_grid_ships(let_ships3))
print(count_uneven_grid_ships(let_ships4))