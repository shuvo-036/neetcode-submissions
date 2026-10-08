class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n= len(prices)
        memo ={}

        def solve(i, buy):

            if i >= n:
                return 0

            if (i, buy) in memo:
                return memo[(i,buy)]

            if buy:
                take = solve(i+1, False) - prices[i]
                skip = solve(i+1 , True)

                memo[(i,buy)] = max(take , skip)
                return memo[(i,buy)]
            else:
                take = solve(i+2, True) + prices[i]
                skip = solve(i+1, False) 
            
                memo[(i,buy)] = max(take , skip)
                return memo[(i,buy)]
        
        return solve(0, True)