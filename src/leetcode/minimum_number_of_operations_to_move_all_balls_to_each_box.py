class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        m = [i for i in range(len(boxes)) if boxes[i] is '1']
        res = [0] * len(boxes)
        
        for i in range(len(res)):
            s = 0
            
            for mi in m:
                if i == mi:
                    continue
                    
                s += abs(i - mi)
            
            res[i] = s
        
        return res
    
"""
n-1
110
1001001
{0:1, 3:1, 6:1}
m = [0,3,6]

for k in m:
    s = 0
    for k2 in m:
        if k == k2:
            continue
            
        s += abs(d[k] - d[k2])
        
    m[k] = s
"""