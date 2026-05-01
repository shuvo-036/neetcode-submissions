class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left =0
        counter =set()
        for right in range(len(nums)):
            if nums[right] in counter:
                return True
            
            counter.add(nums[right])

            if right-left >= k:
                counter.remove(nums[left])
                left +=1
        
        return False