fin  = open("input.txt")
fout = open("output.txt","w")

ch = fin.readline().split()[0]
symbols = 'qwertyuiopasdfghjklzxcvbnm'
next_ch_i = 0

if ch != 'm':
	next_ch_i = symbols.find(ch) + 1

fout.write(symbols[next_ch_i])

fin.close()
fout.close()