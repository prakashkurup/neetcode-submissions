class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS, COLS = len(heights), len(heights[0])
        distArray = [math.inf] * (ROWS * COLS)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        dist, row, col = 0, 0, 0
        distArray[0] = 0
        heap = [(dist, row, col)]
        res = 0

        while heap:
            dist, row, col = heapq.heappop(heap)
            res = max(res, dist)

            if (row, col) == (ROWS - 1, COLS - 1):
                return res

            if dist > distArray[(row * COLS + col)]:
                continue

            for x, y in dirs:
                r, c = row + x, col + y

                if 0 <= r < ROWS and 0 <= c < COLS:
                    newDist = abs(heights[row][col] - heights[r][c])

                    if newDist < distArray[(r * COLS + c)]:
                        distArray[(r * COLS + c)] = newDist
                        heapq.heappush(heap, (newDist, r, c))
