class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        def back(start,target,path):
            if target ==0:
                res.append(path[:])
                return
            
            for i in range(start,len(nums)):
                if nums[i] > target:
                    continue
                path.append(nums[i])
                back(i,target-nums[i],path)
                path.pop()
        back(0,target,[])
        return res
