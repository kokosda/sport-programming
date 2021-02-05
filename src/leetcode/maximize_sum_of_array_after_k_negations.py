class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        len_a = len(A)

        for i in range(len_a):
            if A[i] < 0:
                A[i] = -A[i]
                K -= 1
                
                if K == 0:
                    break
                    
                continue
            
            break
            
        if K > 0:
            idx_of_min, idx_of_zero = 0, -1

            for i in range(1, len_a):
                if A[i] < A[idx_of_min]:
                    idx_of_min = i

                if A[i] == 0:
                    idx_of_zero = i

            if K % 2 == 0:
                if A[idx_of_min] < 0 and idx_of_zero > -1:
                    A[idx_of_min] = -A[idx_of_min]
            else:
                if A[idx_of_min] < 0 or (A[idx_of_min] > 0 and idx_of_zero == -1):
                    A[idx_of_min] = -A[idx_of_min]
            
        return sum(A)
    
    
"""
K=2
[-1,2,3] -> [1,2,3]

[-1]
1
[1]
1
[0]
1
[-2,-4,-7,-3,-1,0,2]
1
[-2,-4,-7,-3,-1,0,2]
3
[-2,-4,-7,-3,-1,0,2]
20
[-2,-4,-7,-3,-1,0,2]
21
[-2,-4,-7,-3,-1]
20
[2,-3,-1,5,-4]
2
[3,-1,0,2]
3
[4,2,3]
1
"""