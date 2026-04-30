class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start =0
        curr_gas=0

        if sum(cost) > sum(gas):
            return -1

        for i in range(len(gas)):

            curr_gas += cgas[i] - cost[i]
            if curr_gas < 0:
                curr_gas =0
                start = i+1

        return start        

        
