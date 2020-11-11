fin  = open("input.txt")
h, m = map(int, fin.readline().split(':'))

h_counter, m_counter, is_found = 23, m, False

if m_counter == 59:
    m_counter = 0
    h = 0 if h == 23 else h + 1
else:
    m_counter += 1

while h_counter >= 0 and not is_found:
    while m_counter < 60:
        formatted_time = str(h).zfill(2) + ':' + str(m_counter).zfill(2)

        if formatted_time[0] == formatted_time[4] and formatted_time[1] == formatted_time[3]:
            is_found = True
            print(formatted_time)
            break

        m_counter += 1

    if h == 23:
        h = 0
    else:
        h += 1

    h_counter -= 1
    m_counter = 0

fin.close()