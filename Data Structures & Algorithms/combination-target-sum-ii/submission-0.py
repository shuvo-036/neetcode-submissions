class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res =[]

        def solve(start , target, path):

            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    continue
                
                path.append(candidates[i])
                solve(i+1, target- candidates[i] , path)
                path.pop()
        solve(0, target,[])
        return res