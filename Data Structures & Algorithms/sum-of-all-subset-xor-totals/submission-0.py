class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n= len(nums)

        def dfs(i, curr_xor):
            if i == n:
                return curr_xor
            
            take = dfs(i+1, curr_xor ^ nums[i])
            skip = dfs(i+1, curr_xor)

            return take + skip
        return dfs(0,0)
                