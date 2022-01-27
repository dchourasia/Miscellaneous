from matrix import *
import math

v1 = [1, 2, 3]
v2 = [4, 5, 6]

def cross_product(x, y):
	m = [[1, 1, 1], x, y]
	cross = [pow(-1, n)*determinant(get_sub_matrix(m, 0, n)) for n in range(0, len(m))]
	return cross
	
	
def dot_product(x, y):
	dot = sum([a*b for a, b in zip(x, y)])
	return dot
	
def add_vectors(*v):
	res = [0]*len(v[0])
	for vector in v:
		res = [a+b for a, b in zip(res, vector)]
	return res
	
def get_length(v):
	length = math.sqrt(sum([x*x for x in v]))
	return length
	
def get_angle_between(x, y):
	theta = math.acos(dot_product(x, y)/(get_length(x)*get_length(y)))
	return theta
	
print(cross_product(v1, v2))
print(dot_product(v1, v2))
print(dot_product(v1, cross_product(v1, v2)))

print(get_angle_between(v1, v2)*180/math.pi)

