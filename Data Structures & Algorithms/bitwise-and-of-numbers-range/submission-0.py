class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        zero = 0
        while left != right:
            left >>= 1
            right >>=1
            zero +=1
        return right << zero