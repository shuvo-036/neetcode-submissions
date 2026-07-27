class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        dp =[[-1] * (amount+1) for _ in range(n)]

        def solve(i,amount):

            if i == n:
                return 0
            
            if amount ==0:
                return 1
            
            if dp[i][amount] != -1:
                return sp[i][amount]
            
            if coins[i] > amount:
                dp[i][amount] = solve(i+1, amount)
                return dp[i][amount]
            
            take = solve(i, amount- coins[i])
            skip = solve(i+1, amount)

            dp[i][amount] = take + skip
            return dp[i][amount]
        
        return solve(0, amount)

            