class Solution:
    def checkValidString(self, s: str) -> bool:

        memo ={}
        def solve(i,open):

            if i == len(s):
                return open == 0
            
            if (i,open) in memo:
                return memo[(i,open)]

            if s[i] == "(":
                memo[(i,open)] = solve(i +1, open +1)
                return memo[(i,open)]
            elif s[i] == ")":
                if open > 0:
                    memo[(i,open)] = solve(i+1, open -1)
                    return memo[(i,open)]               
                return False
            else:
                valid1 = solve(i+1, open)
                valid2 = solve(i+1, open +1)
                valid3 = False
                if open > 0:
                    valid3 = solve(i+1, open-1)
                
                memo[(i,open)] =valid1 or valid2 or valid3
                return memo[(i,open)]
                
        return solve(0, 0)




