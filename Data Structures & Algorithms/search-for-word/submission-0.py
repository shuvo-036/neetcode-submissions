class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def back(r,c,i):
            if i == len(word):
                return True
            if r<0 or c<0 or r >= row or c >= col or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            found=(
                (r+1,c,i+1) or 
                (r-1,c,i+1) or 
                (r,c+1,i+1) or 
                (r,c-1,i+1)
            )

            board[r][c] = temp
            return found
        for r in range(row):
            for c in range(col):
                if back(r,c,0):
                    return True
        
        return False