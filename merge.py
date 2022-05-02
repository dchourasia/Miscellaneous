def mergeSort(a):
	if len(a) == 1:
		return 
	mid = len(a)//2
	left = a[0:mid]
	right = a[mid:len(a)]
	
	mergeSort(left)
	mergeSort(right)
	
	merge(a, left, right)
	
	
def merge(a, left, right):
	x, y, z = 0, 0, 0
	while y < len(left) and z < len(right):
		if left[y] < right[z]:
			a[y] = left[y]
			y += 1
		else:
			a[z] = right[z]
			z += 1
		x += 1