class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):       
                res[i][j] = matrix[j][i]
                
        return res
    
"""
1  2  3   4
5  6  7   8
9  10 11 12

1 5 9
2 6 10
3 7 11
4 8 12

1 4 7
2 5 8
3 6 9
"""