class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        def dfs(i):
            if i ==n:
                return 1
            
            if s[i] == "0":
                return 0

            count = dfs(i+1)

            if i+1 <n:

                if s[i] == "1" or (s[i] =="2" and s[i+1] <= "6"):
                    count += dfs(i+2)
                
            return count
        return dfs(0)