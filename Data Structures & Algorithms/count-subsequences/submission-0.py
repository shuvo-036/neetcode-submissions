class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)

        memo ={}

        def solve(i,j):

            if j ==n:
                return 1

            if i == m:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            if s[i] == t[j]:
                take = solve(i+1,j+1)
                not_take = solve(i+1, j)

                memo[(i,j)] = take + not_take
                return memo[(i,j)]
            else:
                memo[(i,j)] = solve(i+1,j)
                return memo[(i,j)]
        return solve(0,0)
