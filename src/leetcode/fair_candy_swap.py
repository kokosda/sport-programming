class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        set_b = set(B)
        avg_ab = (sum_a + sum_b) // 2
        
        res = []
        
        for i in range(len(A)):
            el = avg_ab - (sum_a - A[i])
            
            if el in set_b:
                res.append(A[i])
                res.append(el)
                break
        
        return res
    
"""
[1,2,5] - [2,4]
8         6
7+1       2+4
6+2       2+4
3+[5]     2+[4]

1,2,5
2,4
avg: 7

7-1=6 6 is in 2,4? no
7-2=5 5 is in 2,5? yes 2 + 5 = 7? yes

1,2
2,3
avg: 4

4-1=3 3 is in 2,3? yes 2 + 3 = 4? no
4-2=2 2 is in 2,3? yes 2 + 3 = 4? no

s1: 3
s2: 5
3-1+(4-2)=2+2
s1-A[i]+(avg-diff) == avg
s1-A[i]-diff = 0
3-1-2=0
3-2+(4-2)=1+2

8-1=7 7==avg no
8-2=6 7>6 check {1,1,4} to have 7-6=1: avg-(sum1-A[i]) in set2
1,-2-,5 -> 1,1,5
1,1,4 -> 1,2,4
s1 = 8
s2 = 6
avg; 7
diff: 2
s1-A[i]-diff = 0
8-2-6=1

[1,1]
[2,2]
[1,2]
[2,3]
[2]
[1,3]
[1,2,5]
[2,4]
"""