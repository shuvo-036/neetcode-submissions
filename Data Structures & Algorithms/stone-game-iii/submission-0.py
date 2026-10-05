class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        memo ={}

        def solve(i):
            
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            res = stoneValue[i] - solve(i+1)

            if i +1 < n:
                res = max(res, stoneValue[i] + stoneValue[i+1] - solve(i+2))
            
            if i+2 < n:
                res = max(res, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]- solve(i+3))
            
            memo[i] = res
            return res
        score = solve(0)

        if score == 0:
            return "Tie"
        elif score < 0:
            return "Bob"
        else:
            return "Alice"