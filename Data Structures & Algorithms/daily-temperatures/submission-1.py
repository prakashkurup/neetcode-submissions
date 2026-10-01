class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                days = index - stack[-1]
                res[stack[-1]] = days
                stack.pop()

            stack.append(index)

        return res