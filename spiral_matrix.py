a = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
        
b = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
     
import math    
def get_next(m):
	rmax, cmax = len(m) -1, len(m[0]) - 1
	idx = [0, 0]
	min = 0
	incr = 1
	stride = 1
	covered = []
	total, curr = (rmax + 1) * (cmax + 1),  0
	rmin, cmin = min, min
	maxes = [rmax, cmax]
	mins = [rmin, cmin]
	while curr < total:
		yield idx[0], idx[1]
		covered.append(str(idx[0]) + str(idx[1]))
		idx[incr] = idx[incr] + stride
		curr += 1
		
		next_idx = idx.copy()
		next_idx[incr] += stride
		if (incr == 0 and idx[incr] in [min, rmax]) or (incr == 1 and idx[incr] in [min, cmax]):
			incr = abs(incr - 1)
		if str(next_idx[0]) + str(next_idx[1]) in covered:
			if stride < 0:
				mins[incr] -= stride
			else:
				maxes[incr] -= stride
			incr = abs(incr - 1)
		if idx == maxes or idx == mins:
			stride *= -1
	#print(covered)
for i, j in get_next(b):
	print(b[i][j], end='\t')
	#print(i, j)

			
	
	
	