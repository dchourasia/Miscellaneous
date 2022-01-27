mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
       
def shiftByK(m, k):
	r = [row[k:] + row[:k] for row in m]
	return r
	
for r in shiftByK(mat, 2):
	print(r)
	