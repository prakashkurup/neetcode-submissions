class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            flag = True
            while stack and ast < 0:
                if stack[-1] > 0:
                    if stack[-1] < abs(ast):
                        stack.pop()
                    elif stack[-1] == abs(ast):
                        stack.pop()
                        flag = False
                        break
                    else:
                        flag = False
                        break
                else:
                    break

            if flag:
                stack.append(ast)

        return stack
                

        
