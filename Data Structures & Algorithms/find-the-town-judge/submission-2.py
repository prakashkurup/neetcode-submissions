class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adj = {node : [] for node in range(1, n + 1)}
        for a, b in trust:
            adj[a].append(b)

        res = -1

        indegree = defaultdict(int)
        for u in adj:
            if adj[u] == []:
                res = u
            for v in adj[u]:
                indegree[v] += 1

        if indegree[res] == n - 1:
            return res

        return -1

        