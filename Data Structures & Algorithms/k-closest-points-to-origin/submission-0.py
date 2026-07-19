class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap =[]

        for point in points:

            x, y = point
            d = x*x + y*y
            heapq.heappush(heap, (-d, x,y))

            if len(heap) > k:
                heapq.heappop(heap)
            
        res= []
        while heap:
            d, x,y = heapq.heappop(heap)

            res.append([x,y])
        return res