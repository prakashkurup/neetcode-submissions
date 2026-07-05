class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = defaultdict(list)
        for word in wordList:
            for index in range(len(word)):
                w = word[:index] + '#' + word[index + 1:]
                adj[w].append(word)

        steps = 1
        q = deque()
        q.append([beginWord, steps])
        visited = set()
        visited.add(beginWord)

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            for index in range(len(word)):
                w = word[:index] + '#' + word[index + 1:]
                
                for nei in adj[w]:
                    if nei not in visited:
                        q.append([nei, steps + 1])
                        visited.add(nei)

        return 0