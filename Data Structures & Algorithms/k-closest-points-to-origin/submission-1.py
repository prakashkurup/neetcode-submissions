class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            x, y = point
            return (x ** 2 + y ** 2)

        left, right = 0, len(points) - 1

        while left <= right:
            pivot = points[right]
            pivotDist = getDistance(pivot)
            p = left

            for index in range(left, right):
                dist = getDistance(points[index])

                if dist < pivotDist:
                    points[p], points[index] = points[index], points[p]
                    p += 1

            points[p], points[right] = points[right], points[p]

            if k < p:
                right = p - 1
            elif k > p:
                left = p + 1
            else:
                return points[:p]

        return points
