class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(x, y):
            return (x ** 2 + y ** 2)

        heap = []

        for x, y in points:
            dist = getDistance(x, y)

            heapq.heappush(heap, [-dist, [x, y]])

            if len(heap) > k:
                heapq.heappop(heap)

        res = [p for _, p in heap]

        return res