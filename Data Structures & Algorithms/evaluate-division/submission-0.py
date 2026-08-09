class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)
        for eq, val in zip(equations, values):
            a, b = eq
            adj[a].append((b, val))
            adj[b].append((a, 1 / val))

        res = [-1.0] * len(queries)

        def dfs(src, dst):
            stack = [(src, 1.0)]
            visited = set([src])

            while stack:
                node, val = stack.pop()

                if node == dst:
                    return val

                for nei, v in adj[node]:
                    if nei not in visited:
                        stack.append((nei, v * val))
                        visited.add(nei)

            return -1.0

        for index, query in enumerate(queries):
            a, b = query
            if a not in adj or b not in adj:
                continue

            visited = {}
            res[index] = dfs(a, b)

        return res