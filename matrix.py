import random


m1 = [[x, x+1, x+2] for x in [1, 4, 7]]
unit = [[1 if i+x==0 else 0 for i in [-1, -2, -3]] for x in [1, 2, 3]]
zero = [[0, 0, 0] for x in [0, 0, 0]]
#print(m1)

def get_zero_matrix(m, n):
	res = [[0 for x in range(0, n)] for y in range(0, m)]
	
	return res
	
def print_mat(m):
	for row in m:
		print(*row, sep='\t')
	print()
#print_mat(unit)

def is_matrix(m):
	res = isinstance(m, list)
	if res and isinstance(m[0], list):
		size = len(m[0])
		for row in m:
			res = size == len(row)
			if not res:
				break
	elif res and isinstance(m[0], (int, float)):
			for row in m:
				res = isinstance(row, (int, float))
				if not res:
					break
	else:
		res = False
					
	return res
			
def multiply_with_scalar(m, s):
		if is_matrix(m):		
			m = [[s*m[x][y] for y in range(0,   len(m[0]))] for x in range(0, len(m))]
			
		return m
		
def round_matrix(m, decimals):
		if is_matrix(m):
			r = get_rank(m)
			m = [[round(m[x][y], decimals) for y in range(0, r)] for x in range(0, r)]
			m = [[round(0.00, decimals) if m[x][y] == 0 else m[x][y] for y in range(0, r)] for x in range(0, r)]
		return m
		
def is_equal(x, y):
	res = is_matrix(x) and is_matrix(y)
	if res:
		for a, b in zip(x, y):
			res = is_equal(a, b)
			if not res:
				break
	if not res and isinstance(x, (int, float)) and isinstance(y, (int, float)):
		res = x == y
				
	return res

def ero_add(m, src, target):
	if is_matrix(m) and len(m) > src and len(m) > target:
		if isinstance(m[0], list):
			m[target] = [x + y for x, y in zip(m[src], m[target])]
		elif isinstance(m[0], (int, float)):
			m[target] = m[target] + m[src]
			
	return m
	
def ero_multiply(m, target, multiplier):
	if is_matrix(m)  and len(m) > target:
		if isinstance(m[0], list):
			m[target] = list(map(lambda x: x*multiplier, m[target]))
		elif isinstance(m[0], (int, float)):
			m[target] = m[target]*multiplier
			
	return m	

def ero_swap(m, x, y):
	if is_matrix(m) and len(m) > x and len(m) > y:
		m[x], m[y] = m[y], m[x]
		
	return m
	
def eco_multiply(m, target, multiplier):
	if is_sqr_matrix(m)  and len(m[0]) > target:
		for i, row in enumerate(m):
			m[i] = [n*multiplier if j == target else n for j, n in enumerate(row)]
			
	return m

def eco_add(m, src, target):
	if is_sqr_matrix(m) and len(m[0]) > src and len(m[0]) > target:
		for i, row in enumerate(m):
			m[i] = [n + row[src] if j == target else n for j, n in enumerate(row)]
			
	return m
	
	
def eco_swap(m, x, y):
	if is_sqr_matrix(m) and len(m[0]) > x and len(m[0]) > y:
		for i, row in enumerate(m):
			row[x], row[y] = row[y], row[x]
			m[i] = row
			
	return m
	
	
	
	
	
def add_matrices(*matrices):
	x, y = len(matrices[0]), len(matrices[0][0])
	res = get_zero_matrix(x, y)
	for m in matrices:
		if mylen(m) == x and y == mylen(m[0]):
			for rows in zip(m, res):
				res.append([a+b for a, b in zip(rows[0], rows[1])])
		else:
			print('matrices are not even sized, first is ', x, y, ' and second is ', len(m), len(m[0]))
			
	return res
	
def mylen(x):
	res = -1
	if isinstance(x, (list, str, dict)):
		res = len(x)
		
	return res
	
def is_identity_matrix(m):
	res = False
	if is_sqr_matrix(m):
		a =1
def multiply_matrices(a, b):
	r = [[] for x in range(0, len(a))]
	#r[0][0] = 9
	#print(r)
	for i in range(0, len(a)):
		for j in range(0, len(b[0])):
			#print(i, j)
			r[i].append(sum([a[i][x]*b[x][j] for x in range(0, len(b))]))
			
	return r		

def determinant(m):
	res = 0
	r = get_rank(m)
	if r > 1:
		all = [n for n in range(0, r)]
		for i, v in enumerate(m[0]):
			res = res + v*pow(-1, i)*determinant(get_sub_matrix(m, 0, i))
	elif r == 1:
		res = m[0][0]
	
	return res
	
def get_rank(m):
	rank = -1
	if is_sqr_matrix(m):
		rank = len(m)
		
	return rank

def get_sub_matrix(m, r, c):
	s = get_rank(m)
	# r'th row and c'th column to be skipped
	if s > 1 and r<s and c < s:
		res = [[x for i, x in enumerate(m[j]) if i != c] for j in range(0, s) if j != r]
		return res
		
		
def is_sqr_matrix(m):
	res = False
	if isinstance(m, list) and len(m) > 0 and isinstance(m[0], list) and len(m) == len(m[0]):
		res = True
		for row in m:
			res = res and len(m) == len(row)
			
	return res
	
def get_sqr_matrix(n):
	res = [[x for x in range(y, y + n)] for y in [z*n + 1 for z in range(0, n)]]
	return res
	
a=[1, 2, 3]
b = [4, 5, 6]

def get_random_sqr_matrix(n):
	res = [[random.randint(y, y + n) for x in range(y, y + n)] for y in [z*n + 1 for z in range(0, n)]]
	
	return res
	
	
def get_identity_matrix(n):
	res = [[1 if x - y == 0 else 0 for x in range(1, n+1)] for y in range(1, n+1)]
	
	return res
	
def transpose(m):
	if is_matrix(m):
		r = get_rank(m)
		c = len(m[0])
		
		tr = [[m[x][y] for x in range(0, r)] for y in range(0, c)]
		
		return tr
		
def get_inverse(m):
	if is_sqr_matrix(m):
		r = get_rank(m)
		det = determinant(m)
		if det != 0:
			inverse = [[pow(-1, x+y)*determinant(get_sub_matrix(m, x, y)) for y in range(0, r)] for x in range(0, r)]
			inverse = multiply_with_scalar(inverse, 1/det)
			inverse = transpose(inverse)
			
			return inverse
		else:
			raise Exception(' not an invertible matrix')
		
"""
def get_inverse(m):
	if is_sqr_matrix(m):
		r = get_rank(m)
		i = get_identity_matrix(r)
		diagonal = [m[x][x] for x in range(0, r)]
		if 0 in diagonal:
			raise Exception('matrix not invertible')
			
		for x in range(0, r):
			for y in range(0, r):
				if x != y and m[x][y] != 0:
					m = eco_multiply(m, y, -m[x][x]/m[x][y])
					m = eco_add(m, x, y)
					
					i = eco_multiply(i, y, -m[x][x]/m[x][y])
					i = eco_add(i, x, y)
			m = eco_multiply(m, x, 1/m[x][x])
					
					
					
			
		print_mat(m)
		print_mat(i)
					
"""			
		#
		#devide nth row by xn
	
#print(list(zip(a, b)))
#print_mat(m1)
#print()
#print_mat(add_matrices(m1, unit, m1))
#print()

#print_mat(multiply_matrices(m1, unit))

#print()

#print_mat(multiply_matrices(m1, m1))

#print(determinant(add_matrices(m1, unit)))

#print(determinant(unit))
#print(is_sqr_matrix(m1))

#print_mat(get_sub_matrix(m1, 1))

#print_mat(get_sqr_matrix(5))

#print(determinant(get_sqr_matrix(5)))

#print_mat(get_random_sqr_matrix(3))

#print(determinant(get_random_sqr_matrix(5)))

#print_mat(get_identity_matrix(5))
#print(is_matrix(m1))
#print(is_equal(m1, m1))
#print(is_equal(m1, unit))

a = [1, 2, 3, 4, 5, 6]

#filtered = filter(lambda x: x%2 == 0, a)
#print(list(filtered))
#transformed = map(lambda x: x*5, a)
#print(list(transformed))

x = 10/7
#print(7*x)
#x1		x2		x3
#y1		y2		y3
#z1		z2		z3


#x1		0		x3
#x1		0		0
#1		0		0

#0		y2		y3
#0		y2		0
#0		1		0

#0		z2		z3
#0		0		z3
#0		0		1
if __name__ == '__main__':
	m = get_random_sqr_matrix(5)
	print_mat(m)
	inv = get_inverse(m)
	print_mat(inv) #print_mat(round_matrix(multiply_matrices(m, inv), 2))

	m = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
	print_mat(get_inverse(m))