n, k = map(int, input().split(' '))
res = (n * (n - 1) // 2) - k
print(res)
"""
Эти числа удовлетворяют ограничениям: 2 < N ≤ 20000; 0 ≤ 2K ≤ N. В каждой следующей строке записан номер группы, затем — количество групп, на которые она разбивается, потом идут пары чисел, разделенные пробелами — номер и численность каждой новой группы. Гарантируется, что если группа Y получилась в результате разбиения группы X, то описание разбиения группы X будет раньше описания разбиения группы Y. Это, в частности, означает, что описание группы 1 расположено во второй строке. Если группа Y получилась в результате разбиения группы X, но её описания не последовало, — это означает, что группа Y больше не разбивалась.

3 0 (n & k)
1 (#) 2 (число групп) (2 (#) 2 (числ)) (3 (#) 1)
2 (#) 2 (число групп) (4 (#) 1 (числ.)) (5 (#) 1)

n * (n - 1) / 2

 1 2 3 4
 1 2
 1 3
 1 4
 2 3
 2 4
 3 4
"""