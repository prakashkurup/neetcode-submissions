class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c : set() for w in words for c in w}
        indegree = {c : 0 for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            minLength = min(len(w1), len(w2))
            for j in range(minLength):
                c1, c2 = w1[j], w2[j]

                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1

                    break

        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegree):
            return ""

        return ''.join(res)