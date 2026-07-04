class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust) < n - 1:
            return -1

        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for node in range(1, n + 1):
            if indegree[node] == n - 1 and outdegree[node] == 0:
                return node

        return -1

        