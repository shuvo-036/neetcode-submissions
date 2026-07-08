"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        intervals.sort(key= lambda x : x.end)
        ans =[]
        ans.append(intervals[0])
        curr_end = intervals[0].end
        n = len(intervals)
        count =0

        for i in range(1,n):
            start ,end = intervals[i].start, intervals[i].end
            if curr_end <= start:
                ans.append(intervals[i])
                curr_end = end
            else:
                i +=1
                count +=1

        return 1 + count 