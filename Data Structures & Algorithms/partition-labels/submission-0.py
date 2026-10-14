class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        memo ={}
        for i in range(len(s)):
            memo[s[i]] = i
        
        start = 0
        end =0
        res =[]

        for i in range(len(s)):
            
            ch = s[i]
            end = max(end, memo[ch])

            if i == end:
                res.append(end - start +1)
                start = i +1
        return res