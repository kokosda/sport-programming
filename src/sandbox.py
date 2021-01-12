bit = 0
n = 5
sum_a = [0] * (1 << n)
w = dict()

for a in range(1, 1 << n):
    print(f'one 1 << ({bit} + 1) = {1 << (bit + 1)}')
    if a == 1 << (bit + 1):
        bit += 1
        w[bit] = 1
        print(f'two bit={bit}, a={a}')
    print(f'three {a} ^ (1 << {bit}) = {a ^ (1 << bit)}')
    sum_a[a] = sum_a[a ^ (1 << bit)] + (w[bit] if w.get(bit) else 0)
    print(f'four {sum_a}')

print(sum_a)