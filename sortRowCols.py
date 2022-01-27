mat = [[3, 2, 1],
  		  [9, 8, 7],
  		  [6, 5, 4]]
  		  
  	
def sortRC(m):
	m = [sorted(row) for row in m]
	for i in range(len(m[0])):
		l = [row[i] for row in m]
		l = sorted(l, reverse=True)
		for idx, row in enumerate(m):
			row[i] = l[idx]
	print(m)
	
sortRC(mat)