class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        target = total // 2

        n= len(stones)

        def solve(i,target):
            if i == n:
                return 0

            if target == 0:
                return 0

            res = solve(i+1,target)

            if stones[i] <= target:
                res = max(res, stones[i]+solve(i+1,target-stones[i]))

            return res

        best = solve(0,target)
        return total - 2* best