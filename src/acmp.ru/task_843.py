fin = open('input.txt')
n, m, f, l = map(int, fin.readline().split())

passed_at_least_one = n - l
passed_all = m + f - passed_at_least_one
only_math = m - passed_all
only_physics = f - passed_all

print(passed_all, only_math, only_physics)

fin.close()