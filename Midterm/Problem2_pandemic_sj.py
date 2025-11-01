def count_infected_neighbors(grid, row, col, n):
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            count += 1
    
    return count

def simulate_pandemic(n, infected_coords):
    grid = [[0] * n for _ in range(n)]
    
    for row, col in infected_coords:
        grid[row][col] = 1
    
    while True:
        new_infections = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    if count_infected_neighbors(grid, i, j, n) >= 2:
                        new_infections.append((i, j))
        
        if not new_infections:
            break
        
        for row, col in new_infections:
            grid[row][col] = 1
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return "There are healthy counties left"
    
    return "There are no healthy counties left"

files = ['pandemic_input1.txt', 'pandemic_input2.txt']
results = []

for filename in files:
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    n = int(lines[0])
    infected_coords = []
    for i in range(1, len(lines)):
        if lines[i].strip():
            row, col = map(int, lines[i].strip().split())
            infected_coords.append((row, col))
    
    result = simulate_pandemic(n, infected_coords)
    results.append(f"Testing {filename}: {result}")

for r in results:
    print(r)

# Save to file
with open('pandemic_output.txt', 'w') as f:
    f.write('\n'.join(results))
