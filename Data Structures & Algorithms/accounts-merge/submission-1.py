class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        adj = defaultdict(set)

        for acc in accounts:
            name = acc[0]
            firstEmail = acc[1]

            for email in acc[1:]:
                if email == firstEmail:
                    continue

                adj[firstEmail].add(email)
                adj[email].add(firstEmail)

        def dfs(email):
            if email in visited:
                return

            visited.add(email)

            for nei in adj[email]:
                dfs(nei)

            emailList.append(email)

        res = []
        visited = set()

        for acc in accounts:
            name = acc[0]
            emailList = []

            for email in acc[1:]:
                dfs(email)

            if emailList:
                res.append([name] + sorted(emailList))

        return res