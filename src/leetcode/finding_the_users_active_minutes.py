class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        used_times = dict() # { ID: { times } }
        
        for log in logs:
            user_id = log[0]
            minute = log[1]
            
            if used_times.get(user_id) is None:
                used_times[user_id] = set()
                
            used_times[user_id].add(minute)
        
        res = [0] * k
        
        for key in used_times:
            mins = len(used_times[key])
            
            if mins > k:
                continue
                
            res[mins - 1] += 1
    
        return res
"""
0: 2, 5
1: 2, 3, 4

[0,1,1,0,0]

0: 2, 5
1: 2, 3

[[0,5],[1,2],[0,2],[0,5],[1,3]]
[0,2,0,0,0]
"""
