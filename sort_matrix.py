mat = [ [ 5, 4, 7 ],
      	  [ 1, 3, 8 ],
      	  [ 2, 9, 6 ] ]
      	  
def sortMatrix(m):
	'''
	def updateDict(idx, val):
		res[idx] = val
	res ={}
	[ updateDict(int(str(i) + str(idx)), e) for idx, row in enumerate(m) for i, e in enumerate(row)]
	res = dict(sorted(res.items(), key=lambda x: x[1]))
	print(res)
	'''
	all = [x for row in m for x in row]
	all.sort()
	l = len(m)
	for i in range(l):
		for j in range(l):
			m[i][j] = all.pop(0)
	return m

mat = sortMatrix(mat)
for row in mat:
	print(row)