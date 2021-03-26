class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        len_row = len(M)
        len_col = len(M[0])
        last_row_idx = len_row - 1
        last_col_idx = len_col - 1
        res = [[0] * len_col for _ in range(len_row)]
        
        for  i in range(len_row):
            for j in range(len_col):
                sum_cur = M[i][j]
                count = 1
                
                if i > 0:
                    sum_cur += M[i - 1][j]
                    count += 1
                if i < last_row_idx:
                    sum_cur += M[i + 1][j]
                    count += 1
                if j > 0:
                    sum_cur += M[i][j - 1]
                    count += 1
                if j < last_col_idx:
                    sum_cur += M[i][j + 1]
                    count += 1
                if i > 0 and j > 0:
                    sum_cur += M[i - 1][j - 1]
                    count += 1
                if i > 0 and j < last_col_idx:
                    sum_cur += M[i - 1][j + 1]
                    count += 1
                if i < last_row_idx and j > 0:
                    sum_cur += M[i + 1][j - 1]
                    count += 1
                if i < last_row_idx and j < last_col_idx:
                    sum_cur += M[i + 1][j + 1]
                    count += 1
                    
                res[i][j] = int(sum_cur / count)
                
        return res
                    