#create a counter
#use nested loops, by length of the grid
# if the element = s, check if it is a start of a ship or just a single S

# if i is 0, which means we are at the most left of the grid, 
# OR the element of the left of the S is = '.' 
# AND
# if j is 0, which means we are at the most left of the grid, OR element below S is '.'
# if true, increase count by 1

# return count

def count_ships(grid):
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 'S':
                if (row == 0 or grid[row-1][column] == '.') and (column == 0 or grid[row][column-1] == '.'):
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

print(count_ships(let_ships))
print(count_ships(let_ships2))
print(count_ships(let_ships3))
print(count_ships(let_ships4))

