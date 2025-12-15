import sys


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    m = int(next(it))
    n = int(next(it))

    grid = [[0] * n for _ in range(m)]
    cells = []

    for i in range(m):
        for j in range(n):
            v = int(next(it))
            grid[i][j] = v
            cells.append((v, i, j))

    # dp[i][j] = max number of steps (edges) starting at (i, j)
    dp = [[0] * n for _ in range(m)]
    cells.sort()

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    best = 0
    for v, i, j in cells:
        cur = 0
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < v:
                cur = max(cur, dp[ni][nj] + 1)
        dp[i][j] = cur
        best = max(best, cur)

    print(best)


if __name__ == "__main__":
    main()
