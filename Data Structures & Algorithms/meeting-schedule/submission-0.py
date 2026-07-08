"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x :x.end)
        n= len(intervals)
        ans = intervals[0].end

        for i in range(1,n):
            start, end = intervals[i].start, intervals[i].end
            if ans < start:
                ans = end
            else:
                return False
        
        return True
