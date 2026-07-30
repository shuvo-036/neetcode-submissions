class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        n = len(s)
        dp = [None] * n

        def dfs(start):
            if start == n:
                return True
            
            if dp[start] is not None:
                return dp[start]

            for end in range(start+1, n+1):
                if s[start:end] in words:
                    if dfs(end):
                        dp[start] = True
                        return True

            dp[start] =  False
            return False

        return dfs(0)