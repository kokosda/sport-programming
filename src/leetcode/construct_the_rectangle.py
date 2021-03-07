class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(sqrt(area)) + 1, 0, -1):
            if area % i == 0:
                j = area // i
                
                if j > i:
                    return [j, i]
                else:
                    return [i, j]
            
        return [0, 0]
    
"""
6
4
5
37
122122
1
2
3
7
10
200
"""