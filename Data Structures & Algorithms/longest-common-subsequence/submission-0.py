class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m= len(text1)
        n = len(text2)

        def solve(m,n):
            if  m==0 or n==0:
                return 0
            
            if text1[m-1] == text2[n-1]:
                return 1 + solve(m-1,n-1)
            else:
                return max(solve(m-1,n) , solve(m,n-1))

        return solve(m,n)