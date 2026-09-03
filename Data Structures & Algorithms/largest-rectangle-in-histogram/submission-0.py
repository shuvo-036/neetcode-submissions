class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        nsl =[]
        stack =[]
        for i in range(n):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if not stack:
                nsl.append(-1)
            else:
                nsl.append(stack[-1][1])

            stack.append((heights[i], i))
        
        nsr =[]
        stack =[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if not stack:
                nsr.append(n)
            else:
                nsr.append(stack[-1][1])
            stack.append((heights[i],i))

        nsr.reverse()

        ans =0
        amount =0
        for i in range(n):
            amount = (nsr[i] - nsl[i]-1) * heights[i]
            ans = max(ans, amount)
        return ans