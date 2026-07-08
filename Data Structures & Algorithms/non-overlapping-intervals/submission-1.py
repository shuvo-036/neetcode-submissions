class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        curr_end = intervals[0][1]
        intervals.sort(key = lambda x :x[1])
        n = len(intervals)
        remove =0

        for i in range(1,n):
            start ,end  = intervals[i]

            if curr_end <= start :
                curr_end = end
            
            else:
                remove +=1
        return remove   