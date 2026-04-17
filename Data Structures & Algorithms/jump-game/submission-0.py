class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fartest = 0
        for i in range(len(nums)):
            if i > fartest:
                return False
            fartest = max(fartest , nums[i] + i)
        return True        