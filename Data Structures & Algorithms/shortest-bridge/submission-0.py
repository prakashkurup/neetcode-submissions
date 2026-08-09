class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        visited = set()

        def dfs(row, col):
            stack = [(row, col)]
            visited.add((row, col))
            q.append((row, col))

            while stack:
                ro, co = stack.pop()

                for x, y in dirs:
                    r, c = ro + x, co + y

                    if 0 <= r < ROWS and 0 <= c < COLS and \
                        grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        stack.append((r, c))
                        visited.add((r, c))

        def bfs():
            count = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    for x, y in dirs:
                        r, c = row + x, col + y

                        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                            continue

                        if grid[r][c] == 1 and (r, c) not in visited:
                            return count

                        if grid[r][c] == 0:
                            grid[r][c] = 1
                            q.append((r, c))
                            visited.add((r, c))

                count += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
        

