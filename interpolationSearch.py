arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
       

def interpolationSearch(a, v):
	res = -1
	l = len(a)
	s, e = 0, l - 1
	approx =int((v - a[s])*l/(a[e] - a[s]) - 1)
	st, e = 1, l - 1
	if v < a[approx]:
		st, e= -1, 0
	print(st, e)
	for i in range(approx, e, st):
		if a[i] == v:
			res = i
			break
	print(approx)
	return res
	
	
print(interpolationSearch(arr, 25))
	