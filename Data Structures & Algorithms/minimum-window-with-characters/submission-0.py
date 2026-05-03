class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        left =0
        res =""
        freq ={}
        need = Counter(t)
        form =0
        min_len =float('inf')
        req = len(need)
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            if s[right] in need and freq[s[right]] == need[s[right]]:
                form +=1
            while form == req:
                if min_len > right -left +1:
                    min_len = min(min_len,right-left+1)
                    res = s[left:right+1]
                freq[s[left]] -=1
                if s[left] in need and freq[s[left]] < need[s[left]]:
                    form -=1
                left +=1
                
        return res