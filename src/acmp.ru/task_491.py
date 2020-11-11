def is_palyndrome(s):
    i, len_s = 0, len(s)

    while i <= len_s - i - 1:
        if s[i] != s[len_s - i - 1]:
            return False
        i += 1

    return True

fin  = open("input.txt")
s = fin.readline().strip()

if is_palyndrome(s):
    char, contains_all_the_same = s[0], True

    for i in range(1, len(s)):
        if s[i] != char:
            contains_all_the_same = False
            break

    if contains_all_the_same:
        print('NO SOLUTION')
    else:
        print(s[:len(s) - 1])
else:
    print(s)

fin.close()