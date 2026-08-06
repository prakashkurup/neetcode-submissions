class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(row, col):
            stack = [(row, col)]
            visited = set()
            visited.add((row, col))
            perimeter = 0

            while stack:
                ro, co = stack.pop()

                for x, y in dirs:
                    r, c = ro + x, co + y

                    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                        perimeter += 1
                        continue

                    if grid[r][c] == 0:
                        perimeter += 1
                    elif grid[r][c] == 1 and (r, c) not in visited:
                        stack.append((r, c))
                        visited.add((r, c))

            return perimeter


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0