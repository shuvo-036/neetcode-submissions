class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        n = len(s)

        def dfs(start):
            if start == n:
                return True
            
            for end in range(start+1, n+1):
                if s[start:end] in words:
                    if dfs(end):
                        return True
            
            return False
        
        return dfs(0)