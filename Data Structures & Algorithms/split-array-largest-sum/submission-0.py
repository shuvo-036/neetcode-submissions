class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) //2

            current = 0
            ops =1
            for num in nums:
                if current + num > mid:
                    ops +=1
                    curernt =0
                
                current += num
            
            if ops <= k:
                right = mid -1
            else:
                left = mid +1
            
        return left 