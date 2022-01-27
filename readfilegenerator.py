def readrow(file):
	for row in open(file):
		yield row
		
print(readrow('1.txt').__next__())

for i in readrow('1.txt'):
	print(i)