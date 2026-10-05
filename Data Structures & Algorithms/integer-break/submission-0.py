class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo ={}

        def solve(n):
            if n ==1:
                return 1

            if n in memo:
                return memo[n]

            res = float("-inf")
            for i in range(1,n):
                prod = i * max(n-i, solve(n-i))
                res = max(res, prod)

            memo[n] =res
            return res
        return solve(n)
