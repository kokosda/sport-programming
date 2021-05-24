from typing import List

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 == date2:
            return 0
        
        months = self.get_days_in_month()
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        
        if y1 > y2:
            y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1
        elif m1 > m2:
            y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1
        elif d1 > d2:
            y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1
        
        res = 0
        
        leap_days = 0
        
        if self.is_leap(y1):
            if m1 <= 2 and d1 <= 28 and (y2 > y1 or m2 > 2):
                leap_days += 1
                
        if self.is_leap(y2):
            if (y2 > y1 or m1 <= 2 and d1 <= 28) and (d2 == 29 or m2 > 2):
                leap_days += 1
                
        yt = y1 + 4 - y1 % 4
        
        while yt < y2:
            if self.is_leap(yt):
                leap_days += 1

            yt += 4

        res = (y2 - y1) * 365 + leap_days
        
        m_max = max(m1, m2)
        m_min = min(m1, m2) + 1
        m_days = 0
        
        while m_min < m_max:
            m_days += months[m_min]
            m_min += 1
            
        if m1 > m2:
            m_min = -m_min
            
        res += m_days
        
        if m1 != m2:
            res += months[m1] - d1
            
        res += d2
        return res
        
    def get_days_in_month(self) -> List[int]:
        res = [31] * 13
        thirty_days_month = { 4, 6, 9, 11 }
        
        for i in range(1, 13):
            if i in thirty_days_month:
                res[i] = 30
        
        res[2] = 28
        return res
    
    def is_leap(self, year: int) -> bool:
        res = year % 4 is 0 and year % 100 is not 0 or year % 400 is 0
        return res
    
solution = Solution()
solution.daysBetweenDates('2023-03-05', '2001-01-17')


from datetime import date

print(date(2023, 3, 5) - date(2001, 1, 17))