class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)

        if "0000" in dead:
            return -1
        
        q = deque()
        visited =set(["0000"])
        q.append("0000")
        

        moves = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return moves
                for i in range(4):
                    num = int(curr[i])
                    for ch in [-1,+1]:
                        newnum = (ch+ num) % 10  
                        newstate = curr[:i] + str(newnum) + curr[i+1:]

                        if newstate not in dead and newstate not in visited:
                            q.append(newstate)
                            visited.add(newstate)
            moves +=1
        return -1