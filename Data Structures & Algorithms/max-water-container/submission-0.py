class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights) 
        r= n-1
        max_area =0
        while l<r:
            w = r-l
            h= min(heights[l] , heights[r])
            a= w *h
            max_area = max(max_area , a)

            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return max_area            