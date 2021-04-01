class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ZERO_SHIFT = 0
        
        for shift_i in range(m):
            diag = self._get_diag(mat, shift_i, ZERO_SHIFT, m, n)
            diag.sort()
            self._set_diag(diag, mat, shift_i, ZERO_SHIFT, m, n)
            
        for shift_i in range(1, n):
            diag = self._get_diag(mat, ZERO_SHIFT, shift_i, m, n)
            diag.sort()
            self._set_diag(diag, mat, ZERO_SHIFT, shift_i, m, n)
              
        return mat
    
    def _get_diag(self, mat, shift_i, shift_j, m, n):
        diag = []
        i = shift_i
        j = shift_j

        while i < m and j < n:
            diag.append(mat[i][j])
            i += 1
            j += 1
            
        return diag
    
    def _set_diag(self, diag, mat, shift_i, shift_j, m, n):
        i = shift_i
        j = shift_j
        cur_di = 0
        
        while i < m and j < n:
            mat[i][j] = diag[cur_di]
            i += 1
            j += 1
            cur_di += 1
        
"""
[
    [11,25,66,1, 69,7],
    [23,55,17,45,15,52],
    [75,31,36,44,58,8],
    [22,27,33,25,68,4],
    [84,28,14,11,5,50]
]

    [75,31,36,44] [14,11,25,44]
    [22,27,33,25] [22,27,31,36]
    [84,28,14,11] [84,28,75,33]
"""