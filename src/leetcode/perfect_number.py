class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        divs_sum = 0
        
        for i in range(2, int(sqrt(num) + 1)):
            div, mod = divmod(num, i)
            
            if mod is 0:
                divs_sum += div
                divs_sum += num // div
                
        return (divs_sum + 1) == num