class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_len = len(image)
        col_len = len(image[0])
        last_row_idx, last_col_idx = row_len - 1, col_len - 1
        src_color = image[sr][sc]
        
        if src_color == newColor:
            return image
        
        def dfs(i, j):
            if image[i][j] != src_color:
                return
            
            image[i][j] = newColor
            
            if i > 0:
                dfs(i - 1, j)
            if j > 0:
                dfs(i, j - 1)
            if i < last_row_idx:
                dfs(i + 1, j)
            if j < last_col_idx:
                dfs(i, j + 1)
            
        dfs(sr, sc)        
        return image
        
"""
1 1 1
1 1 0
1 0 1

2

2 2 2
2 2 0
2 0 1
"""