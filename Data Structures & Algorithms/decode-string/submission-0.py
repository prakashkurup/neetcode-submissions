class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        num = 0
        curr_str = ''

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if c == '[':
                    stack.append([curr_str, num])
                    curr_str = ''
                    num = 0
                
                elif c == ']':
                    prev_str, count = stack.pop()
                    curr_str = prev_str + curr_str * count
                
                else:
                    curr_str += c

        return curr_str
