"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key= lambda x : x.end)
        ans =[]
        ans.append(intervals[0])
        curr_end = intervals[0].end
        n = len(intervals)

        for i in range(1,n):
            start ,end = intervals[i].start, intervals[i].end
            if curr_end <= start:
                ans.append(intervals[i])
                curr_end = end
            else:
                i +=1

        return len(ans)