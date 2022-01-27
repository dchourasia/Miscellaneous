matrix =[
            [1,  2,  3,  4 ], # i = 1, j = 1-4
            [5,  6,  7,  8 ],  # i = 2, j = 1-4
            [9,  10, 11, 12 ],  #i = 3, j = 1-4
            [13, 14, 15, 16 ] # i = 4, j = 1-4
        ]
  
#  i min -> j max -> i max -> j min
def fetch(a):
	for x in a:
		yield x
		
def extract(m, s, e):
  r =[]
  covered =[]
  # i min
  i = s
  for j in range(s, e+1):
  	r.append(m[i][j])
  	covered.append(i + 10*j)
  	
  # j max
  for i in range(s, e+1):
  	if i + 10*j not in covered:
  		r.append(m[i][j])
  		covered.append(i + 10*j)
  		
  # i max
  for j in range(e, s - 1, -1):
  	if i + 10*j not in covered:
  		r.append(m[i][j])
  		covered.append(i + 10*j)
  		
  # j min
  for i in range(e, s - 1, -1):
  	if i + 10*j not in covered:
  		r.append(m[i][j])
  		covered.append(i + 10*j)
  
  print(r)
  r = r[-1:] + r[0:-1]
  print(r)
  f = fetch(r)
  
  covered =[]
  # i min
  i = s
  for j in range(s, e+1):
  	m[i][j] = next(f)
  	covered.append(i + 10*j)
  	
  # j max
  for i in range(s, e+1):
  	if i + 10*j not in covered:
  		m[i][j] = next(f)
  		covered.append(i + 10*j)
  		
  # i max
  for j in range(e, s - 1, -1):
  	if i + 10*j not in covered:
  		m[i][j] = next(f)
  		covered.append(i + 10*j)
  		
  # j min
  for i in range(e, s - 1, -1):
  	if i + 10*j not in covered:
  		m[i][j] = next(f)
  		covered.append(i + 10*j)
  
  return m
  	
  	
d, s, e = 100, 0, len(matrix) -1
while d >= 1:
	matrix = extract(matrix, s, e) 
	s += 1
	e -= 1
	d = e - s
	
for x in matrix:
	print(x)

