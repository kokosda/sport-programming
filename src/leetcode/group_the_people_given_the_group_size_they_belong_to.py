class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = dict()
        
        for i in range(len(groupSizes)):
            gs = groupSizes[i]
            group = None
            
            if groups.get(gs) is None:
                groups[gs] = []
                group = []
                groups[gs].append(group)
            else:
                group = groups[gs][-1]
            
            if len(group) < gs:
                group.append(i)
            else:
                group = []
                groups[gs].append(group)
                group.append(i)
            
        res = []
        
        for k in groups:
            for g in groups[k]:
                res.append(g)
                
        return res
        