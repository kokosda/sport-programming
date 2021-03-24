class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        min_x, min_y = points[0], points[0]
        max_x, max_y = points[0], points[0]
        
        for p in points:
            if min_x[0] > p[0]:
                min_x = p
            if min_y[1] > p[1]:
                min_y = p
            if max_x[0] < p[0]:
                max_x = p
            if max_y[1] < p[1]:
                max_y = p
                
        res = 0
        #print(min_x, min_y, max_x, max_y)
                
        for ep in [min_x, min_y, max_x, max_y]:
            for p1 in points:
                if p1 is ep:
                    continue
                    
                for p2 in points:
                    if p2 is ep or p2 is p1:
                        continue
                        
                    l1 = sqrt((ep[0] - p1[0]) ** 2 + (ep[1] - p1[1]) ** 2)
                    l2 = sqrt((ep[0] - p2[0]) ** 2 + (ep[1] - p2[1]) ** 2)
                    l3 = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
                    pm = (l1 + l2 + l3) / 2
                    sq = pm * (pm - l1) * (pm - l2) * (pm - l3)
                    
                    if sq < 0:                        
                        #print(pm, l1, l2, l3, ep, p1, p2)
                        pass
                    else:
                        res = max(res, sq)
                        
        res = sqrt(res)
        return res
    
"""
[[0,0],[0,1],[1,0],[0,2],[2,0]]
[[5,1],[41,-3],[38,5],[-44,-39],[14,4],[23,45],[35,3],[33,-43],[41,2],[-1,-15],[47,33],[-49,9],[6,25],[-3,10]]
"""