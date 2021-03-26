class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2:
            return []
        
        d1 = { list1[i]:i for i in range(len(list1)) }
        d2 = { list2[i]:i for i in range(len(list2)) }
        
        if len(list1) != len(list2):
            d1, d2 = (d1, d2) if len(list1) <= len(list2) else (d2, d1)
            
        min_order = 10 ** 4
        
        for k in d1:
            if d2.get(k, -1) >= 0:
                min_order = min(min_order, d1[k] + d2[k])
                d1[k] += d2[k]
            else:
                d1[k] = -1
                
        res = []
        
        for k in d1:
            if d1[k] == min_order:
                res.append(k)
                
        return res
