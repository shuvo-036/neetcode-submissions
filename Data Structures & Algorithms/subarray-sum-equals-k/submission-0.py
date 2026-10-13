class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        res = 0
        seen = {0: 1}

        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - k in seen:
                res += seen[curr_sum - k]

            seen[curr_sum] = seen.get(curr_sum, 0) + 1

        return res