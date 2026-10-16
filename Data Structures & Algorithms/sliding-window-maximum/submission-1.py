class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        n= len(nums)
        i= 0
        j =0
        dq = deque()
        res =[]

        while j <n:
            while dq and dq[-1] < nums[j]:
                dq.pop()
            
            dq.append(nums[j])

            if j -i +1 < k:
                j +=1
            elif j -i +1 ==k:
                res.append(dq[0])

                i +=1
                j +=1

        return res