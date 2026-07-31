class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
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

        count = 0

        while q:
            node = q.popleft()
            count += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return count == numCourses