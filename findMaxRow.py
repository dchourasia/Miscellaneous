mat = [[0, 0, 0, 1],
       	[0, 1, 1, 1],
     	  [1, 1, 1, 1],
      	 [0, 0, 0, 0]]
      	 
def findMaxRow(m, num):
      	 maxes = [row.count(num) for row in m]
      	 mx = max(maxes)
      	 max_row_indices = [idx for idx, val in enumerate(maxes) if val == mx]
      	 return max_row_indices
      	 
print(findMaxRow(mat, 1))
print('I have found the max row')
      	 
      	 