class Solution:
    def validPalindrome(self, s: str) -> bool:
         
        l =0
        r = len(s)-1

        def palin(l,r):
            while l<=r:
                if s[l].lower() != s[r].lower():
                    return False

                l +=1
                r -=1
            return True    

        while l<=r:
            if s[l].lower() == s[r].lower():
                return True
            else:
                return palin(l+1,r) or palin(l,r-1)

                
            return True 