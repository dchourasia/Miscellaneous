s='hello world! 123'

#print(ord('9'))
num=0
chr=0
for c in s:
	if 48 <= ord(c) <= 58:
		num += 1
	else:
		chr += 1
		
print('Found', num, 'numbers and ', chr, ' characters.')
	









