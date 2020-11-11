n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

p_set = set(p[1:])
union = p_set.union(q[1:])

if len(union) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')