class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        adj = defaultdict(list)
        visited = set()
        res = []

        for account in accounts:
            name = account[0]
            firstEmail = account[1]

            for email in account[1:]:
                if email != firstEmail:
                    adj[firstEmail].append(email)
                    adj[email].append(firstEmail)

        '''
        neet@gmail.com      : neet_dsa@gmail.com, bob@gmail.com
        neet_dsa@gmail.com  : neet@gmail.com,
        bob@gmail.com       : neet@gmail.com,
        neet@gmail.com      : bob@gmail.com
        '''

        def dfs(node, curr):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei, curr)

            curr.append(node)

        for account in accounts:
            name = account[0]
            curr = []

            for email in account[1:]:
                if email not in visited:
                    dfs(email, curr)

            if curr:
                res.append([name] + curr[:])
        
        return res