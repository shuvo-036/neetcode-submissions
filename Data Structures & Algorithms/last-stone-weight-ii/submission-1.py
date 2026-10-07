class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        target = total // 2

        memo = {}

        def solve(i, target):
            if i == len(stones):
                return 0

            if target == 0:
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i,target)] = solve(i+1, target)

            if stones[i] <= target:
                memo[(i,target)] = max(memo[(i,target)], stones[i] + solve(i+1, target-stones[i]))

            return memo[(i,target)]
        
        best = solve(0, target)
        return total - 2 * best