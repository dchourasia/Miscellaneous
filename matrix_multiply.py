A = [[1, 2, 3],
    	 [4, 5, 6],
  	   [7, 8, 9]]
  	   
B = [[1, 2, 3],
  	   [4, 5, 6],
 	    [7, 8, 9]]
 	    
def multiply_matrices(m, n):
	def multiplyRow(i, j):
		return sum([m[i][k] * n[k][j] for k in range(len(m[i]))])
		
	if len(m[0]) != len(n):
		raise(Exception('matrices are not compatible to get multiplied'))
	#mult = [[]] * len(m) # this creates all the list obj by ref, means changing one object will chang3 all the list objects
	mult = [[] for x in range(len(m))]
	r, c = len(m), len(n[0])
	#print(r, c)
#	print(mult)
	for i in range(r):
		for j in range(c):
			#print(i, j)
		#	print(mult)
			mult[i].append(multiplyRow(i, j))
	return mult
			
			
			
C = multiply_matrices(A, B)
for row in C:
	print(row)
		
		
	