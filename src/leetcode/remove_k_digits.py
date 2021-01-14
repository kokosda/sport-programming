class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        if k == 0:
            return num
        
        i = 0
        
        while k > 0 and (i + 1) < len(num):
            if i > 0 and num[i - 1] > num[i]:
                if i - 1 > 0:
                    num = num[:i - 1] + num[i:]
                else:
                    num = num[i:]
                k -= 1
                continue
                
            if num[i + 1] > num[i]:
                if i + 2 < len(num):
                    num = num[:i + 1] + num[i + 2:]
                else:
                    num = num[:i + 1]
                k -= 1
                print(num, '1')
                continue
                
            if num[i] > num[i + 1]:
                if i > 0:
                    num = num[:i] + num[i + 1:]
                else:
                    num = num[1:]
                print(num, '2')
                k -= 1
                continue
                
            i += 1
            
        i = 0
        
        while k > 0 and (i + 1) < len(num):
            if num[i + 1] == num[i]:
                if i + 2 < len(num):
                    num = num[:i + 1] + num[i + 2:]
                else:
                    num = num[:i + 1]
                k -= 1
                print(num, '3')
                continue
            i += 1
            
        if k > 0:
            print(num, k, 'oops')
            
        num = num.lstrip('0')
        
        if len(num) == 0:
            num = '0'
            
        return num
    
"""
num=1432219, k=3
1432219: 1219

num=4432219, k=3
6737219: 

num=111332, k=3
111332: 111

num=111, k=2
111: 1

num=101, k=2
101: 0

num=1021, k=2
1021: 1

"1432219"
3
"4432219"
3
"111332"
3
"111"
2
"101"
2
"1021"
2
"100001"
2
"""