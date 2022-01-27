matrix = [[0, 1, 2],
   	          [3, 4, 5],
    	         [6, 7, 8]]
    	         
a = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
        	      
def swapD(m):
	for i in range(len(m)):
		m[i][i], m[i][3-i] = m[i][3-i], m[i][i]
	for r in m:
		print(r)
	
	
swapD(a)

