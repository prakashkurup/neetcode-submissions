class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1: return [0]
        
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        indegree = [0] * n
        for node in adj:
            indegree[node] += len(adj[node])

        q = deque()
        for node in range(len(indegree)):
            if indegree[node] == 1:
                q.append(node)

        nodesLeft = n
        while nodesLeft > 2:
            qlen = len(q)
            nodesLeft -= qlen

            for _ in range(qlen):
                leaf = q.popleft()

                for nei in adj[leaf]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        return list(q)
