
import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []  
        self.minheap = []  

    def addNum(self, num: int) -> None:

        if len(self.maxheap) == 0 or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap , - heapq.heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap , -heapq.heappop(self.minheap))


    def findMedian(self) -> float:

        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2

        return float(-self.maxheap[0])

