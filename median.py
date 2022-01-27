m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]

def getMedian(m):
	x = sorted([e for row in m for e in row])
	indices = []
	if len(x)%2 == 0:
		indices = [int(len(x)/2) - 1, int(len(x)/2)]
	else:
		indices = [int(len(x)/2)]
		
	return sum([x[idx] for idx in indices])/len(indices)
	
	
print(getMedian(m))
	