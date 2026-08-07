class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        WATER, TREASURE, LAND = -1, 0, (2 ** 31) - 1
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == TREASURE:
                    q.append((r, c, 0))

        while q:
            row, col, steps = q.popleft()
            grid[row][col] = steps

            for x, y in dirs:
                r, c = row + x, col + y

                if 0 <= r < ROWS and 0 <= c < COLS and \
                    grid[r][c] == LAND:
                    grid[r][c] = steps + 1
                    q.append((r, c, steps + 1))
