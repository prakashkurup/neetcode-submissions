class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = { c : set() for w in words for c in w }
        indegree = { c : 0 for w in words for c in w }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            minLen = min(len(w1), len(w2))

            for j in range(minLen):
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
        count = 0

        while q:
            node = q.popleft()
            count += 1
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if count != len(adj):
            return ""

        return ''.join(res)
        