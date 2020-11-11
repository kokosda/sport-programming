from math import sqrt
fin  = open("input.txt")

a = list(map(int, fin.readline().split()))
sum_of_people_per_day = 0

for i in range(len(a)):
    sum_of_people_per_day += a[i]

number_of_people = sum_of_people_per_day // 27

print(number_of_people)

fin.close()