class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        target = sum(matchsticks) //4

        side =[0] * 4
        matchsticks.sort()
        if sum(matchsticks) %4 !=0:
            return False
        
        def solve(i):

            seen = set()
            if i == len(matchsticks):
                return True

            for j in range(4):
                if side[j] in seen:
                    continue
                seen.add(side[j])
                if side[j] + matchsticks[i] <= target:
                    side[j] += matchsticks[i]
                    if solve(i+1):
                        return True

                    side[j] -= matchsticks[i]

            return False

        return solve(0) 