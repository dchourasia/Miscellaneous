m	= [[ 2, 5, 7 ],
  	      [ 3, 7, 2 ], 
	        [ 5, 6, 9 ]]
	        
for i in range(len(m)):
	print(m[i][i]**2)
	
for i in range(len(m)):
	print(m[i][len(m) - 1 - i]**2)