import math

def is_valid_board(n, symbols, board):
    sqrt_n = int(math.sqrt(n))
    
    for row in board:
        seen = set()
        for cell in row:
            if cell != '.' and cell in seen:
                return False
            if cell != '.':
                seen.add(cell)
    
    for col in range(n):
        seen = set()
        for row in range(n):
            cell = board[row][col]
            if cell != '.' and cell in seen:
                return False
            if cell != '.':
                seen.add(cell)

    for box_row in range(0, n, sqrt_n):
        for box_col in range(0, n, sqrt_n):
            seen = set()
            for i in range(box_row, box_row + sqrt_n):
                for j in range(box_col, box_col + sqrt_n):
                    cell = board[i][j]
                    if cell != '.' and cell in seen:
                        return False
                    if cell != '.':
                        seen.add(cell)
    
    return True

files = ['spg_input1.txt', 'spg_input2.txt']
results = []

for filename in files:
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    n = int(lines[0])
    symbols = lines[1].strip().split(',')
    
    board = []
    for i in range(2, len(lines)):
        if lines[i].strip():
            row = lines[i].strip().split(',')
            board.append(row)
    
    if is_valid_board(n, symbols, board):
        result = "The board is valid"
    else:
        result = "The board is invalid"
    
    results.append(f"Testing {filename}: {result}")

for r in results:
    print(r)

# Save to file
with open('symbol_puzzle_output.txt', 'w') as f:
    f.write('\n'.join(results))
