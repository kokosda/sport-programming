class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = dict()
        
        for e in edges:
            d[e[0]] = d.get(e[0], 0) + 1
            d[e[1]] = d.get(e[1], 0) + 1
            
        max_v = 0
        max_v_count = 0
        
        for k in d:
            if max_v_count < d[k]:                
                max_v_count = d[k]
                max_v = k
        
        return max_v