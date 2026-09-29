class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)

        if endWord not in words:
            return 0
        
        visited= set()
        visited.add(beginWord)
        q = deque()
        q.append((beginWord,1))

        while q:
            currword , length = q.popleft()

            if currword == endWord:
                return length

            for i in range(len(currword)):
                for ch in "qwertyuioplkjhgfdsazxcvbnm":
                    if currword[i] == ch:
                        continue
                    newword = currword[:i] + ch + currword[i+1:]

                    if newword in words and newword not in visited:
                        q.append((newword, length+1))
                        visited.add(newword)
        

        return 0