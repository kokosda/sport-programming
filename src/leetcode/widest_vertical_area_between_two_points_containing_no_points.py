class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_s = set()
        res = 0
        nums = []
        
        for i in range(len(points)):
            p = points[i]
            
            if p[0] in x_s:
                continue
                
            heapq.heappush(nums, p[0])
            x_s.add(p[0])
            
        prev_x = heapq.heappop(nums)
        
        while len(nums) > 0:
            cur_x = heapq.heappop(nums)
            res = max(res, cur_x - prev_x)
            prev_x = cur_x
            
        return res