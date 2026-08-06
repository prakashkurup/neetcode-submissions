class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        charIndex = {char : index for index, char in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return False

            minLength = min(len(w1), len(w2))

            for j in range(minLength):
                c1, c2 = w1[j], w2[j]

                if c1 != c2:
                    if charIndex[c1] > charIndex[c2]:
                        return False

                    break
        
        return True