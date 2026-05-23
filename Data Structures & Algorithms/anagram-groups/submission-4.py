class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans ={}


        for s in strs:
            
            sorted_strs = ''.join(sorted(s))
            if sorted_strs not in ans:
                ans[sorted_strs] = []
            
            ans[sorted_strs].append(s)

        return list(ans.values())            