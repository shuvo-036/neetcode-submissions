class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {

                "I":1, "V":5 , "c":100, "X":10,"L":50, "D":500, "M":1000
        } 

        total =0

        for i in range(len(s)):
            if i < len(s) -1 and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total