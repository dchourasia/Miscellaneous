mat = [ [1, 2, 3, 4 ],
             [5, 6, 7, 8 ],
             [9, 10, 11, 12 ],
             [13, 14, 15, 16 ] ]
'''
1x4  1x1
1x3  2x1
1x2  3x1
1x1  4x1

0x0   0x3
0x1   1x3
0x2   2x3
0x3   3x3
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
	for i in range(int(x/2)):
		for j in range(i, x - i - 1):
			print(f'{i}x{j}', end='\t')
			print(f'{j}x{l - i}', end='\t')
			print(f'{l - i}x{l - j}', end='\t')
			print(f'{l - j}x{i}')
			m[i][j], m[j][l - i], m[l - i][l - j], m[l- j][i] = m[j][l - i], m[l - i][l - j], m[l- j][i], m[i][j]
			
	return m
rotate(mat)

for row in mat:
	print(row)
	