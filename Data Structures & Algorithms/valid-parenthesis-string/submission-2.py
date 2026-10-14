class Solution:
    def checkValidString(self, s: str) -> bool:
        
        def solve(i,open):

            if i == len(s):
                return open == 0
            
            if s[i] == "(":
                return solve(i +1, open +1)
            elif s[i] == ")":
                if open > 0:
                    return solve(i+1, open -1)
                return False
            else:
                valid1 = solve(i+1, open)
                valid2 = solve(i+1, open +1)
                valid3 = False
                if open > 0:
                    valid3 = solve(i+1, open-1)
                
                return valid1 or valid2 or valid3
        return solve(0, 0)




