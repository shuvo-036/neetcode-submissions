class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)

        while left <= right:

            mid = (left + right) //2

            current =0
            required_day = 1
            for w in weights:
                if current + w > mid:
                    required_day +=1
                    current =0

                current += w

            if required_day <= days:
                right = mid -1
            else:
                left = mid +1

        return left