class Solution:
    def jump(self, nums: List[int]) -> int:
        jump =0
        curr_end =0
        fartest =0
        for i in range(len(nums)-1):
            fartest = max(fartest , nums[i] +i)

            if i == curr_end:
                jump +=1
                curr_end = fartest
        return jump        
            