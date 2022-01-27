
def multiply(m, n):
	if len(m[0]) != len(n):
		return 
	p = [[] for i in range(len(m))]
	for r in range(len(m)):
		for c in range(len(n[0])):
			p[r].append(sum([m[r][x]*n[x][c] for x in range(len(n))]))
	return p
#	print(p)
	
def isIdentity(m):
	r = len(m)
	res = True
	for i in range(len(m)):
		for j in range(len(m)):
			res = m[i][j] == 1 if i==j else m[i][j]==0
			if not res:
				break
	return res
	
	
m = [[1, 0, 0],
		[0, -1, 0],
		[0, 0, -1]]
		
m = multiply(m, m)
print(isIdentity(m))
		
