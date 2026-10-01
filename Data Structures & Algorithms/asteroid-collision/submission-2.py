class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            alive = True

            while alive and stack and ast < 0 < stack[-1]:
                if stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast):
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(ast)

        return stack
