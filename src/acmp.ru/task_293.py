fin  = open("input.txt")
n = int(fin.readline())
incomes = list(map(int, fin.readline().split()))
taxes = list(map(int, fin.readline().split()))
max_tax_income, max_tax_i = 0, 0

for i in range(n):
	tax_income = (incomes[i] / 100) * taxes[i]
	if tax_income > max_tax_income:
		max_tax_income = tax_income
		max_tax_i = i

print(max_tax_i + 1)
fin.close()