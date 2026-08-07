class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pac, atl = set(), set()

        def dfs(row, col, visited):
            stack = [(row, col)]
            visited.add((row, col))

            while stack:
                ro, co = stack.pop()

                for x, y in dirs:
                    r, c = ro + x, co + y

                    if 0 <= r < ROWS and 0 <= c < COLS and \
                        heights[r][c] >= heights[ro][co] and \
                        (r, c) not in visited:
                        stack.append((r, c))
                        visited.add((r, c))


        for c in range(COLS):
            if (0, c) not in pac:
                dfs(0, c, pac)
            
            if (ROWS - 1, c) not in atl:
                dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            if (r, 0) not in pac:
                dfs(r, 0, pac)

            if (r, COLS - 1) not in atl:
                dfs(r, COLS - 1, atl)

        return list(pac.intersection(atl))

        