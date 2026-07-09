class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            s1 = -1 * heapq.heappop(heap)
            s2 = -1 * heapq.heappop(heap)

            diff = abs(s1 - s2)
            if diff > 0:
                heapq.heappush(heap, -diff)

        return -1 * heap[0] if heap else 0