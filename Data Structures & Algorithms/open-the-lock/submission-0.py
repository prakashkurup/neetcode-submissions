class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deads = set(deadends)
        if '0000' in deads: return -1

        deads.add('0000')

        q = deque()
        steps = 0
        q.append(['0000', steps])

        while q:
            lock, steps = q.popleft()

            if lock == target:
                return steps

            for index in range(len(lock)):
                up = '0' if lock[index] == '9' else str(int(lock[index]) + 1)
                down = '9' if lock[index] == '0' else str(int(lock[index]) - 1)

                l1 = lock[:index] + up + lock[index + 1:]
                l2 = lock[:index] + down + lock[index + 1:]

                if l1 not in deads:
                    q.append([l1, steps + 1])
                    deads.add(l1)
                
                if l2 not in deads:
                    q.append([l2, steps + 1])
                    deads.add(l2)

        return -1

            