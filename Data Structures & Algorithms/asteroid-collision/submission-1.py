class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack =[]

        for x in asteroids:
            while stack and stack[-1] > 0 and x < 0:
                summ = stack[-1] + x

                if summ == 0:
                    x =0
                    stack.pop()
                elif summ >= 0:
                    x =0
                elif summ < 0:
                    stack.pop()
            
            if x != 0:
                stack.append(x)
        
        return stack