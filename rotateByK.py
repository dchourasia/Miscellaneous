mat = [ [1, 2, 3, 4 ],
             [5, 6, 7, 8 ],
             [9, 10, 11, 12 ],
             [13, 14, 15, 16 ] ]
'''
k = 4
ixj      
0x0   1x3
0x1   2x3
0x2   3x3
0x3   3x3

1x3   3x2

 //ixj    4 - j + 1, i   ==>    4 - i + 1, 4 - j + 1 ==> 
         j, 4 - i + 1   ==>    i, j
//ixj     5 - j, i     ==>    5 - i, 5 - j     ==> j, 5 - i  => i, j
ixj     j, 3 - i     ==>    3 - i, 3 - j    ==>  3 - j, i  => i, j

1x1   1x2
1x2   2x2
2x2   2x1
2x1   1x1
'''        
def rotate(m):
	x = len(m)
	l = x - 1
	m = [row[::-1] for row in m[::-1]]
			
	return m
mat = rotate(mat)

for row in mat:
	print(row)
	