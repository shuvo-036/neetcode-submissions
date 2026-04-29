class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = 0
        res =[]
        while l < len(word1) or l < len(word2):
            if l < len(word1):
                res.append(word1[l])
            if l < len(word2):
                res.append(word2[l])    
            
            l +=1
        return "".join(res) 