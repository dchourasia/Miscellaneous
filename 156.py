'''
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''




import math
def get_sum(x):
	print(x)
	return sum([int(c) for c in str(x)])
	
sums = [get_sum(int(math.pow(x, y))) for x in range(1, 10) for y in range(1, 10)]

print(max(sums))
#print(sums)
#print(str(int(pow(99, 99))))