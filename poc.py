import math, itertools

x = str(345**3)

perms = list(itertools.permutations(x))
perms = [''.join(x) for x in perms]
print(len(perms))

p =1
for i in range(1, 9):
	p*=i
print(p)