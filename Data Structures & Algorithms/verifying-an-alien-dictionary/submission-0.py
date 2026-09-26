class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        memo = {}

        for i in range(len(order)):
            memo[order[i]] = i
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if memo[word1[j]] > memo[word2[j]]:
                        return False
                    break
            
            else:
                if len(word1) > len(word2):
                    return False
        return True