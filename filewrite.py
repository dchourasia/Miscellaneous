import os

#print(os.getcwd())

f = open('1.txt', 'w')

l=[i for i in range(1, 100)]

for i in l:
	f.write(str(i) + '\n')