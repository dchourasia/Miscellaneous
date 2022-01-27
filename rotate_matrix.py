mat = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]
        
def rotate(m):
	r = []
	for n in range(len(m) - 1, -1, -1):
		r.append([m[x][n] for x in range(0, len(m))])
	return r
	
	
print(rotate(mat))

