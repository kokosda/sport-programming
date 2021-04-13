class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        i = 0
        j = 1
        
        for k in range(2, len(A) - 1, 2):
            if A[k] == A[k + 1]:
                return A[k]
            
            if A[k] == A[i] or A[k] == A[j]:
                return A[k]
            
            if A[k + 1] == A[i] or A[k + 1] == A[j]:
                print(i, j, k, k + 1)
                return A[k + 1]
            
            i = k
            j = k + 1
        
        return -1
    
"""
a: 2N
unique: N+1
duplic: N-1 + 1

[1,2,3,4,5,6,4,4,4,4]
[5,1,3,2,4,5,5,5]
"""