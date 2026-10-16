class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        ans =[]
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            ans.append(max(window))
        return ans