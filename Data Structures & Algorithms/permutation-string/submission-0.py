class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left =0
        freq ={}
        need = len(s1)
        ned = Counter(s1)
        for right in range(len(s2)):
            freq[s2[right]] = freq.get(s2[right],0)+1

            if right -left +1 > need:
                freq[s2[left]] -=1
                if freq[s2[left]] ==0:
                    del freq[s2[left]]
                
                left +=1

            
            if ned == freq:
                return True
        return False
