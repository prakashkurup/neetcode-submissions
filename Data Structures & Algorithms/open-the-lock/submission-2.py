class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        start = '0000'
        deads = set(deadends)

        if start in deads or target in deads:
            return -1

        q = deque()
        q.append((start, 0))
        deads.add(start)

        while q:
            lock, steps = q.popleft()

            if lock == target:
                return steps

            for index in range(len(lock)):
                up = '0' if lock[index] == '9' else str(int(lock[index]) + 1)
                down = '9' if lock[index] == '0' else str(int(lock[index]) - 1)

                c1 = lock[:index] + up + lock[index + 1:]
                c2 = lock[:index] + down + lock[index + 1:]

                if c1 not in deads:
                    q.append((c1, steps + 1))
                    deads.add(c1)

                if c2 not in deads:
                    q.append((c2, steps + 1))
                    deads.add(c2)

        return -1
                

            