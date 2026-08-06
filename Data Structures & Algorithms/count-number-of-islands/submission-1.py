class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = 0
        visited = set()
        LAND, WATER = "1", "0"

        def bfs(row, col):
            q = deque()
            q.append([row, col])
            visited.add((row, col))

            while q:
                ro, co = q.popleft()

                for x, y in dirs:
                    r, c = ro + x, co + y

                    if 0 <= r < ROWS and 0 <= c < COLS and \
                        grid[r][c] == LAND and (r, c) not in visited:
                        q.append([r, c])
                        visited.add((r, c))

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands