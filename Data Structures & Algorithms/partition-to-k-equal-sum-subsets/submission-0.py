class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)

        if total % k !=0:
            return False
        n = len(nums)
        nums.sort(reverse = True)
        target = total // k
        if nums[0] > target:
            return False

        bucket =[0] *n

        def solve(i):
            if i == n:
                return True
            
            seen = set()
            for j in range(k):
                if bucket[j] in seen:
                    continue
                seen.add(bucket[j])

                if bucket[j] + nums[i] <= target:
                    bucket[j] += nums[i]

                    if solve(i+1):
                        return True
                    
                    bucket[j] -= nums[i]
                
            return False
        
        return solve(0)