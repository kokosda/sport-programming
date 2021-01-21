class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:        
        if len(intervals) == 1:
            return 1
        
        sorted_intervals = (sorted(intervals))
        max_interval = sorted_intervals[0]
        count = 1
        
        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            
            if max_interval[0] <= interval[0] and max_interval[1] >= interval[1]:
                continue
            
            if max_interval[0] < interval[0]:
                count += 1
            
            max_interval = interval
                
        return count
    
"""
[
    [0,2]   [0,2]
    [0,5]   [1,2]
    [1,2]   [2,4]
    [1,5]   [0,5]
    [2,3]   [1,5]
    [2,4]   [2,5]
    [3,4]
    [3,7]   [4,5]
    [4,5]   [3,7]
    
    [a,b) - [2,5]
    [c,d) - [0,5)
    0 <= 2 and 5 <= 5
]

[[0,5],[1,2],[2,4],[2,5]]
[[3,7],[0,5],[1,2],[4,5],[2,5],[0,2],[2,4],[1,5]]
[[3,7],[0,5],[1,2],[4,5],[2,5],[0,2],[2,4],[1,5],[2,6]]
[[3,7],[0,5],[1,2],[4,5],[2,5],[0,2],[2,4],[1,5],[2,6],[4,12]]
[[0,1],[1,2],[2,3]]
[[0,1],[1,2],[2,3],[5,10]]
"""