fin  = open("input.txt")

def split_on_ranges(phone_number, templates):
    ranges = {}
    i = 0

    while i != (len(phone_number) - 1):
        duple = phone_number[i:i + 2]
        key = duple + '_' + str(i) + '_' + str(i + 1)

        if len(duple) == 2:
            if duple[0] == duple[1]:
                ranges[key] = temlpates['aa']

        triple = phone_number[i:i + 3]
        key = triple + '_' + str(i) + '_' + str(i + 2)
        
        if len(triple) == 3:
            if triple[0] != triple[1] and triple[0] == triple[2]:
                ranges[key] = temlpates['aba']
            elif triple[0] == triple[1] and triple[0] != triple[2]:
                ranges[key] = temlpates['aab']
            elif triple[0] != triple[1] and triple[1] == triple[2]:
                ranges[key] = temlpates['abb']
            elif triple[0] == triple[1] and triple[1] == triple[2]:
                ranges[key] = temlpates['aaa']

        quad = phone_number[i:i + 4]
        key = quad + '_' + str(i) + '_' + str(i + 3)

        if len(quad) == 4:
            if quad[0] != quad[1] and quad[0] == quad[2] and quad[1] != quad[3]:
                ranges[key] = temlpates['abac']
            elif quad[0] != quad[1] and quad[1] == quad[3] and quad[0] != quad[2]:
                ranges[key] = temlpates['baca']
            elif quad[0] == quad[2] and quad[1] == quad[3] and quad[0] != quad[1]:
                ranges[key] = temlpates['abab']
            elif quad[0] == quad[1] and quad[2] == quad[3] and quad[0] != quad[2]:
                ranges[key] = temlpates['aabb']
            elif quad[0] == quad[3] and quad[1] == quad[2] and quad[0] != quad[1]:
                ranges[key] = temlpates['abba']
            elif quad[0] != quad[1] and quad[1] == quad[2] and quad[1] == quad[3]:
                ranges[key] = temlpates['baaa']
            elif quad[0] != quad[1] and quad[0] == quad[2] and quad[0] == quad[3]:
                ranges[key] = temlpates['abaa']
            elif quad[0] == quad[1] and quad[0] != quad[2] and quad[0] == quad[3]:
                ranges[key] = temlpates['aaba']
            elif quad[0] == quad[1] and quad[0] == quad[2] and quad[0] != quad[3]:
                ranges[key] = temlpates['aaab']
            elif quad[0] == quad[1] and quad[0] == quad[2] and quad[0] == quad[3]:
                ranges[key] = temlpates['aaaa']

        i += 1

    return ranges

#неоптимальное решение для номера 7277333
def get_ranges_of_highest_points(ranges):
    highest_points_ranges = []

    while len(ranges) > 0:
        max_points = 0
        number, i0, i1, point_value = '', 0, 0, 0

        for k, v in ranges.items():        
            if (max_points < v):
                max_points = v
                number, i0, i1 = k.split('_')
                i0, i1 = int(i0), int(i1)
                point_value = v

        points_removal = []

        for k in ranges:
            _, i0_c, i1_c = k.split('_')
            i0_c, i1_c = int(i0_c), int(i1_c)

            if i1_c < i0 or i0_c > i1:
                continue

            points_removal.append(k)

        for i in points_removal:
            ranges.pop(i)

        highest_points_ranges.append([number, i0, i1, point_value])

    highest_points_ranges.sort(key=lambda slice_number: slice_number[1])
    return highest_points_ranges

phone_number = fin.readline()

temlpates = {
    'aa': 2,
    'aba': 2,
    'aab': 2,
    'abb': 2,
    'aaa': 3,
    'abac': 2,
    'baca': 2,
    'abab': 3,
    'aabb': 3,
    'abba': 4,
    'baaa': 3,
    'abaa': 3,
    'aaba': 3,
    'aaab': 3,
    'aaaa': 5
}

ranges = split_on_ranges(phone_number, temlpates)
print(ranges)
ranges = get_ranges_of_highest_points(ranges)
print(ranges)

phone_number_prettified, point_sum = '', 0
i_p = 0

for i in range(len(ranges)):
    _, i0, i1, point_value = ranges[i]

    if i_p != i0:
        phone_number_prettified += phone_number[i_p:i0] + '-'

    phone_number_prettified += phone_number[i0:i1 + 1]

    if i1 < len(phone_number) - 1:
        phone_number_prettified += '-'

    i_p = i1 + 1
    point_sum += point_value
else:
    phone_number_prettified += phone_number[i_p:]

print(phone_number_prettified)
print(point_sum)

fin.close()

#bruteforce