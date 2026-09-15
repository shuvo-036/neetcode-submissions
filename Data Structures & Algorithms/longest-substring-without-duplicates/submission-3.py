class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left =0
        right =0
        window = set()
        ans =0
        n = len(s)

        while right < n:

            if s[right] not in window:
                window.add(s[right])
                ans = max(ans, right - left +1)
                right +=1

            else:
                window.remove(s[left])
                left +=1
        return ans
