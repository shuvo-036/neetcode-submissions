
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()

                curr = curr.children[ch]

            curr.word = word

        row = len(board)
        col = len(board[0])
        res = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, curr):
            if r < 0 or c < 0 or r >= row or c >= col:
                return

            ch = board[r][c]

            if ch == "#" or ch not in curr.children:
                return

            curr = curr.children[ch]

            if curr.word:
                res.append(curr.word)
                curr.word = None

            board[r][c] = "#"

            for dr, dc in directions:
                dfs(r + dr, c + dc, curr)

            board[r][c] = ch

        for r in range(row):
            for c in range(col):
                dfs(r, c, root)

        return res







