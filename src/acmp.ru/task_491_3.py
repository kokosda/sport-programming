def is_palyndrome(s):
    i, len_s = 0, len(s)

    if len_s == 0:
        return False

    while i <= len_s - i - 1:
        if s[i] != s[len_s - i - 1]:
            return False
        i += 1

    return True

fin  = open("input.txt")
s = fin.readline()

if is_palyndrome(s):
    if len(s) < 3:
        print('NO SOLUTION')
    else:
        char, contains_all_the_same = s[0], True

        for i in range(1, len(s)):
            if s[i] != char:
                contains_all_the_same = False
                break

        if contains_all_the_same:
            print('NO SOLUTION')
        else:
            while is_palyndrome(s):
                s = s[:len(s) - 1]
            
            if len(s) == 0:
                print('NO SOLUTION')
            else:
                print(s)
else:
    print(s)
fin.close()