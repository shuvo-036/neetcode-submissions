class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n= len(coins)
        memo ={}

        def solve(i, amount):
            if amount ==0:
                return 0
            
            if i == n or amount < 0:
                return float('inf')

            if (i,amount) in memo:
                return memo[(i, amount)]

            take = 1 + solve(i, amount- coins[i])
            skip = solve(i+1, amount)

            memo[(i, amount)] = min(take , skip)
            return memo[(i, amount)]
        ans = solve(0, amount)

        if ans == float("inf"):
            return -1
        
        return ans