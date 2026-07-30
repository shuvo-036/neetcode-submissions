class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n= len(nums)
        prefix =1
        suffex =1
        ans = float("-inf")

        for i in range(len(nums)):
            if prefix == 0:
                prefix =1
            if suffex ==0:
                suffex =1
            
            
            prefix *= nums[i]
            suffex *= nums[n-i-1]

            ans = max(ans, max(prefix, suffex))
        return ans