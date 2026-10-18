class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        words = set(dictionary)
        n= len(s)
        memo ={}

        def solve(i):
            if  i>= n:
                return 0
            
            if i in memo:
                return memo[i]

            ans = 1 + solve(i+1)

            for j in range(i,n):
                word = s[i:j+1]

                if word in words:
                    ans = min(ans, solve(j+1))

            memo[i] = ans 
            return ans


        return solve(0)