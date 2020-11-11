fin  = open("input.txt")

n = int(fin.readline())
valid_codes = {}

for i in range(0, 10):
    valid_codes[str(i)] = 'digit'

valid_codes['A'] = 'letter'
valid_codes['B'] = 'letter'
valid_codes['C'] = 'letter'
valid_codes['E'] = 'letter'
valid_codes['H'] = 'letter'
valid_codes['K'] = 'letter'
valid_codes['M'] = 'letter'
valid_codes['O'] = 'letter'
valid_codes['P'] = 'letter'
valid_codes['T'] = 'letter'
valid_codes['X'] = 'letter'
valid_codes['Y'] = 'letter'

for i in range(n):
    s = fin.readline().rstrip()
    is_valid = True

    if len(s) != 6:
        print('No')
        continue

    for j in range(len(s)):
        if (j == 0 or j >= 4 and j <= 5) and valid_codes.get(s[j]) == 'letter':
            continue

        if j >= 1 and j <= 3 and valid_codes.get(s[j]) == 'digit':
            continue

        is_valid = False
        break

    if is_valid:
        print('Yes')
    else:
        print('No')

fin.close()