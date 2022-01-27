mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]
           
    
    
def checkIfCircular(m):
	cts = {x:m[0].count(x) for x in m[0]}
	isCircular = True
	
	for row in m:
		cts1 = {x:m[0].count(x) for x in m[0]}
		isCircular = compareDicts(cts, cts1)
		if not isCircular:
			break
	return isCircular

def compareDicts(c, d):
	equal = len(c) == len(d)
	if equal:
		for x in c:
			try:
				equal = c[x] == d[x]
			except:
				equal = False
			if not equal:
				break
	return equal
	
print(checkIfCircular(mat))