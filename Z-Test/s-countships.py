
def count_ships(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == ".":
            return
        grid[i][j] = "."
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                count += 1
                dfs(i, j)
    print(grid)
    return count

ships = [
    [".", "S", ".", "S"],
    [".", ".", ".", "S"],
    ["S", "S", ".", "S"],
    [".", ".", ".", "S"]
]

print(count_ships(ships))


ships2 = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"]
]
print(count_ships(ships2))


# The function uses a nested function dfs that takes the row and column indices of a cell as input. If the cell is out of bounds or contains a ".", the function returns. Otherwise, it marks the cell as visited by setting it to ".", and then recursively calls itself on its neighboring cells in all four directions.

# The outer loop iterates through each element of the grid, and if it encounters an "S", it increments the count of ships and calls the dfs function on that cell to mark all the cells of the ship as visited.

# Note that the function modifies the input grid by marking the cells of each ship as visited. If you don't want to modify the input grid, you can make a copy of it before calling the function.

# Overall, this approach can be more efficient than the previous approach, especially if the grid contains many ships, since it avoids unnecessary iterations.