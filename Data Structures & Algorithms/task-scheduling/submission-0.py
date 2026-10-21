class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        total = len(tasks)

        freq = sorted(Counter(tasks).values())

        max_freq = freq[-1]
        gap = max_freq -1
        idle = gap *n

        for count in freq[-2::-1]:
            idle -= min(gap, count)
        
        return total + max(0, idle)