e1 = '3x + y = 2'
e2 = 'x + 5y = 20'

#y = x2y1 - x1y2/ x2c1- x1c2
#x = y2x1 - y1x2/ y2c1 - y1c2

import re

def parse_equation(e):
	parts = re.split(r'[+=]', e)
	#print(parts)
	for part in parts:
		part = part.strip()
		last = part[-1].lower()
		if last == 'x':
			x = part.replace('x', '')
			if not x:
				x = 1
		elif last == 'y':
			y = part.replace('y', '')
			if not y:
				y = 1
		else:
			c = part
	return (float(x), float(y), float(c))
def solve_equations(e1, e2):
	p1= parse_equation(e1)
	print(p1)

	p2 = parse_equation(e2)
	print(p2)
	
	x = (p2[1]*p1[0] - p1[1]*p2[0])/(p2[1]*p1[2] - p1[1]*p2[2])
	
	y = (p2[0]*p1[1] - p1[0]*p2[1])/(p2[0]*p1[2] - p1[0]*p2[2])
	
	print('x = ', x)
	print('y = ', y)

solve_equations(e1, e2)