class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right =0

        ans =float("inf")
        total =0

        while right< len(nums):

            total += nums[right]

            
            
            while total >= target:
                ans = min(ans, right- left+1)
                total -= nums[left]
                left +=1
                

            right +=1 

        return 0 if ans == float('inf') else ans