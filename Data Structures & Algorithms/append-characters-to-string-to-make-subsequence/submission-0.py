class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        tIndex = 0

        for i in range(len(s)):
            if s[i] == t[tIndex]:
                tIndex += 1

                if tIndex == len(t):
                    return 0

        return len(t) - tIndex

        