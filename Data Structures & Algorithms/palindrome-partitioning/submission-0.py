class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        path =[]
        res = []

        def solve(s):
            if len(s) == 0:
                res.append(path[:])
                return
            
            for i in range(len(s)):
                substr = s[0:i+1]

                if substr == substr[::-1]:
                    path.append(substr)
                    solve(s[i+1:])
                    path.pop()
            
        solve(s)
        return res