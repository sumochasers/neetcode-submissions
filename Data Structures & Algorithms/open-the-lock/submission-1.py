class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def children(lock : str) -> list[str]:
            res = []
            for i in range(4):
                digit : int = (int(lock[i]) + 1) % 10
                next_digits :str = lock[:i] + str(digit) + lock[i + 1:]
                digit : int = (int(lock[i]) - 1 + 10) % 10 
                prev_digits :str = lock[:i] + str(digit) + lock[i + 1:]
                res.append(next_digits)
                res.append(prev_digits)
            return res
        
        if "0000" in deadends:
            return -1

        q = deque(["0000"])
        visited = set(deadends)
        visited.add("0000")

        level = 0
        while q :
            for _ in range(len(q)):
                node = q.popleft()
                if node == target :
                    return level
                for child in children(node) :
                    if child not in visited :
                        visited.add(child)
                        q.append(child)
            level += 1
        
        return -1 





        