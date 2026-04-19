class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[1] * len(nums)

        pre =1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        suff = 1
        for i in range(len(nums)-1 , -1, -1):
            res[i] *= suff
            suff *= nums[i]

        return res        