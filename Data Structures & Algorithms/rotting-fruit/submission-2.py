class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                if grid[r][c] == FRESH:
                    fresh += 1

        if q == []:
            return -1

        if fresh == 0:
            return 0

        minutes = -1

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                for x, y in dirs:
                    r, c = row + x, col + y

                    if 0 <= r < ROWS and 0 <= c < COLS and \
                        grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        q.append((r, c))
                        fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1