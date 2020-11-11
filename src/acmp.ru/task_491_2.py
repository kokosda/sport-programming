fin  = open("input.txt")
s = fin.readline()

len_s = len(s)
middle = len_s // 2 - 1
mids = [middle, middle + 1]

if len_s % 2 != 0:
    mids[0] = mids[1]

last_idx = len_s - 1

while mids[0] >= 0 and mids[1] <= last_idx and s[mids[0]] == s[mids[1]]:
    mids[0] -= 1
    mids[1] += 1

if mids[0] == -1 and mids[1] == len_s:
    print(s[:last_idx])
else:
    print(s)

fin.close()