class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_x, min_y = m, n
        
        for op in ops:
            min_x = min(min_x, op[0])
            min_y = min(min_y, op[1])
            
        return min_x * min_y
    
    
"""
0 0 0
0 0 0
0 0 0

2,1

1 1 0
0 0 0
0 0 0

1,2

2 1 0
1 0 0
0 0 0

3
3
[[2,2],[3,3],[3,3],[3,3],[2,2],[2,1],[3,3],[3,3],[2,2],[1,3],[3,3],[3,3]]
3
3
[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
3
3
[[2,2],[3,3]]
26
17
[[20,10],[26,11],[2,11],[4,16],[2,3],[23,13],[7,15],[11,11],[25,13],[11,13],[13,11],[13,16],[26,17]]

"""