class Course:
    def __init__(self, duration: int, closedOnDay: int):
        self.duration = duration
        self.closedOnDay = closedOnDay

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1] - x[0])
        total_duration = 0
        count = 0
        
        for c in courses:
            if total_duration + c[0] > c[1]:
                break
                
            total_duration += c[0]
            count += 1
                
        return count
    
"""
[100 (duration), 200 (closed_on)] - 101 finish
[1000, 1250] - 1100 finish
[200, 1300] - 1300 finish

[[100,200],[200,1300],[1000,1250],[2000,3200]]
[[50,20]]
[[10,40],[2,40],[1000,20]]
[[5,5],[4,6],[2,6]] - fails
"""