class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {n : [] for n in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)

        indegree = [0] * numCourses
        for u in adj:
            for v in adj[u]:
                indegree[v] += 1

        q = deque()
        for index in range(len(indegree)):
            if indegree[index] == 0:
                q.append(index)

        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []