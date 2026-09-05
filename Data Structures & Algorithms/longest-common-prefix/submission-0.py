class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s= strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(s):
                s = s[:-1]
                
            if not s:
                return ""
        return s