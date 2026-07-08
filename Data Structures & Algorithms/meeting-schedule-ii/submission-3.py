"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush , heappop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        intervals.sort(key= lambda x : x.start)
        heap =[]
        heappush(heap, intervals[0].end)
        n = len(intervals)

        for i in range(1,n):
            start ,end = intervals[i].start , intervals[i].end
            if heap[0] <= start:
                heappop(heap)
            heappush(heap ,end)
        
        return len(heap)
                