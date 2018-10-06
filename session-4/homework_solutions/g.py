grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
        
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
    
print("\nAlternatively, we could do this: \n")
for i in range(len(grid[0])):
    line = ''
    for j in range(len(grid)):
        line = line + grid[j][i]
    print(line)