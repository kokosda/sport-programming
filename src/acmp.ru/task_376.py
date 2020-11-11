from datetime import date

def is_leap_year(year):
    result = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    return result

def get_next_leap_year(year):
    while True:
        year += 1

        if is_leap_year(year):
            return year

fin = open('input.txt')
bd, bm = map(int, fin.readline().split())
cd, cm, cy = map(int, fin.readline().split())

by = cy

if bm == 2 and bd == 29:
    if not is_leap_year(by) or bm < cm:
        by = get_next_leap_year(by)

b_date = date(by, bm, bd)
c_date = date(cy, cm, cd)
diff = c_date - b_date

if diff.days <= 0:
    print(abs(diff.days))
else:
    b_date = date(by + 1, bm, bd)
    diff = c_date - b_date
    print(abs(diff.days))

fin.close()
