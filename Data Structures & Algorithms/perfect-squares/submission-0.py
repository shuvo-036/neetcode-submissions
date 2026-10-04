class Solution:
    def numSquares(self, n: int) -> int:
        
        dp ={}

        def solve(n):

            if n == 0:
                return 0

            if n in dp:
                return dp[n]

            res = float("inf")

            for i in range(1,int(n ** 0.5)+1):
                squre = i *i
                res = min(res , 1 +solve( n - squre))

            dp[n] = res
            return dp[n] 
        return solve(n)


