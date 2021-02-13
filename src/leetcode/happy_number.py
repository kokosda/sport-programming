class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        s = str(n)

        while True:
            res = 0
            
            for i in s:
                res += int(i)**2
            
            if res == 1:
                return True
            
            if res not in store:
                store.add(res)
                s = str(res)
            else:
                return False
                
            
"""
10011

0001
1001

101
1 + 0 + 1 = 2
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0 = 4
"""