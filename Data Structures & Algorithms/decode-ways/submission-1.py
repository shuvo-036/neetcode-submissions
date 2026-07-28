class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [-1] * n

        def dfs(i):
            if i ==n:
                return 1
            
            if s[i] == "0":
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = dfs(i+1)

            if i+1 <n:

                if s[i] == "1" or (s[i] =="2" and s[i+1] <= "6"):
                    dp[i] += dfs(i+2)
                    

            return dp[i]
        return dfs(0)