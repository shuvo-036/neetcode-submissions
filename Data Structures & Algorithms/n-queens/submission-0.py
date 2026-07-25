class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res =[]
        board = [["."] *n for _ in range(n)]


        cols =set()
        posdia =set()
        antidia =set()

        def back(row):

            if row ==n:
                path = ["".join(r) for r in board]
                res.append(path)
                return
            
            for col in range(n):
                if col in cols or (row+col) in posdia or (row-col) in antidia:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                posdia.add(row+ col)
                antidia.add(row-col)

                back(row +1)

                board[row][col] = "."
                cols.remove(col)
                posdia.remove(row+ col)
                antidia.remove(row-col)
                
        
        back(0)
        return res
