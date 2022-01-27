mat = [ [ 5, 4, 7 ],
      	  [ 1, 3, 8 ],
      	  [ 2, 9, 6 ] ]
      	  
def sortMatrix(m):
	def updateDict(idx, val):
		res[idx] = val
	res ={}
	[ updateDict(int(str(i) + str(idx)), e) for idx, row in enumerate(m) for i, e in enumerate(row)]
	res = dict(sorted(res.items(), key=lambda x: x[1]))
	print(res)
	

	
	
x = [1, 3]
y= [2]
#y.append(*x)
print(y)
y.extend(x)
print(y)
sortMatrix(mat)