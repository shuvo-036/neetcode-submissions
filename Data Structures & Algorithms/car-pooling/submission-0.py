class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        event = [0] * 1001

        for passenger , start , end in trips:
            event[start] += passenger
            event[end] -= passenger
        
        change = 0
        for i in range(len(event)):
            change += event[i]

            if change > capacity:
                return False

        return True