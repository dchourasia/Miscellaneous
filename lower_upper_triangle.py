matrix = [[1, 2, 3],
         		 [4, 5, 6],
     		     [7, 8, 9]];
     		     
def lower_triangle(m):
	for i in range(len(m)):
		for j in range(i+1, len(m)):
			m[i][j] = 0
	return m

def upper_triangle(m):
	for i in range(len(m)):
		for j in range(i):
			m[i][j] = 0
	return m
	
m = lower_triangle(matrix.copy())

for row in m:
	print(row)
	
m = upper_triangle(matrix.copy())

for row in m:
	print(row)