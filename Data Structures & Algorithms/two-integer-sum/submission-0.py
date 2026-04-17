class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}

        for i in range(len(nums)):
            if target-nums[i] in has:
                return [has[target-nums[i]] ,i]
            has[nums[i]] = i    

          