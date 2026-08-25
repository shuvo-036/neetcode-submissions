import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap =[]

        for num in arr:
            heapq.heappush(heap, (abs(num - x), num))

        ans = []

        for _ in range(k):
            dist , num = heapq.heappop(heap)
            ans.append(num)

        ans.sort()
        return ans        