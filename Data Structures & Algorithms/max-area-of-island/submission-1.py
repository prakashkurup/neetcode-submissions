class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        maxArea = 0
        visited = set()
        LAND, WATER = 1, 0

        def bfs(row, col):
            q = deque()
            q.append([row, col])
            visited.add((row, col))
            count = 1

            while q:
                ro, co = q.popleft()

                for x, y in dirs:
                    r, c = ro + x, co + y

                    if 0 <= r < ROWS and 0 <= c < COLS and \
                        grid[r][c] == LAND and (r, c) not in visited:
                        q.append([r, c])
                        visited.add((r, c))
                        count += 1

            return count

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
