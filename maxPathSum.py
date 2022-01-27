mat = ([[ 10, 10, 2, 0, 20, 4 ],
   		     [ 1, 0, 0, 30, 2, 5 ],
  		      [ 0, 10, 4, 0, 2, 0 ],
  		      [ 100, 0, 2, 20, 0, 4 ]])
  		      

  		      
 
def findAllPaths(m):
	cmin, cmax = 0, len(m[0]) - 1
	s = [[(0, c)] for c in range(len(m[0]))]
	for i in range(len(m) - 1):
		s1 = [p + [(p[-1][0] + 1, p[-1][1] - 1)] for p in s if p[-1][1] > cmin]
		s2 = [p + [(p[-1][0] + 1, p[-1][1])] for p in s]
		s3 = [p + [(p[-1][0] + 1, p[-1][1] + 1)] for p in s if p[-1][1] < cmax]
		s = s1 + s2 + s3
		
	print('total paths', len(s))
	return s
	
	
paths = findAllPaths(mat)
sums = {}
for i, path in enumerate(paths):
	vals = [mat[r][c] for r, c in path]
	sums[i] = sum(vals)
	
mkey = max(sums, key=sums.get)
print(paths[mkey], sums[mkey])
	
		