class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n= len(nums)
        total_sum = n* (n+1)//2
        ans = total_sum -sum(nums)
        return ans