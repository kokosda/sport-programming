class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0, 0, 0]
        result = True
        
        for bill in bills:
            if bill == 5:
                cash[0] += 1
            elif bill == 10:
                if cash[0] > 0:
                    cash[0] -= 1
                    cash[1] += 1
                else:
                    result = False
                    break
            elif bill == 20:
                if cash[1] > 0 and cash[0] > 0:
                    cash[0] -= 1
                    cash[1] -= 1
                    cash[2] += 1
                elif cash[0] >= 3:
                    cash[0] -= 3
                    cash[2] += 1
                else:
                    result = False
                    break
                    
            
        return result