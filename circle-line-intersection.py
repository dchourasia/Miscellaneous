e1 = 'x  + y = 10'
center = (0, 0)
radius = 10

#y = x2y1 - x1y2/ x2c1- x1c2
#x = y2x1 - y1x2/ y2c1 - y1c2

import re
import math

def parse_equation(e):
	e = e.replace(' ', '')
	parts = re.split(r'[xy=]', e)
	print(parts)
	parts = [p + '1' if p in '+-' else p for p in parts]
	parts = ['1' if p is '' else p for p in parts]
	
	
	x = parts[0]
	y = parts[1]
	c = parts[3]
	return float(x), float(y), float(c)
	
p = parse_equation(e1)
print(p)

def solve_quadratic_equation(a, b, c):
	b24ac = math.sqrt(b*b - 4*a*c)
	
	x1 = (-b + b24ac)/(2*a)
	x2 = (-b - b24ac)/(2*a)
	
	return x1, x2
	
def get_circle_line_intersection(r, x, y, z):
	a = x*x + y*y
	b = -2*x*z
	c = z*z - y*y*r*r
	print('a, b, c', a, b, c)
	x1, x2 = solve_quadratic_equation(a, b, c)
	print(x1, x2)
	y1 = (z - x*x1)/y
	y2 = (z - x*x2)/y
	
	print('first intersection', x1, y1)
	print('seconf intersection', x2, y2)

x, y, c = parse_equation(e1)
get_circle_line_intersection(radius, x, y, c)
print(solve_quadratic_equation(1, -3, 2))
