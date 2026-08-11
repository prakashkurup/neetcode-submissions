class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        original = image[sr][sc]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        image[sr][sc] = color
        q = deque()
        q.append((sr, sc))

        while q:
            row, col = q.popleft()
            
            for x, y in dirs:
                r, c = row + x, col + y

                if 0 <= r < ROWS and 0 <= c < COLS and \
                    image[r][c] == original:
                    image[r][c] = color
                    q.append((r, c))

        return image
