#2D list

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 9, 10],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)

for row in number_grid:
     print(row)    