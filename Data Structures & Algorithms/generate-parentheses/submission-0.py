class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def solve(openn, close, curr ):

            if openn ==0 and close ==0:
                res.append(curr)
                return

            if openn > 0:
                solve(openn -1 , close, curr +"(")
            if close > openn:
                solve(openn, close-1 , curr +")")
            
        solve(n,n,"")
        return res