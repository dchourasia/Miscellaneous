cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
def mergeSort(a):
	if len(a) <= 1:
		return 
	
	mid = len(a)//2
	x = a[:mid]
	y = a[mid:]
	
	mergeSort(x)
	mergeSort(y)
	
	merge(x, y, a)
	
	
def merge(x, y, a):
	i = j = k = 0
	print('=============')
	print(x, y)
	while i < len(x) and j < len(y):
		print(i, j, k)
		if x[i] < y [j]:
				a[k] = x[i]
				i += 1
		else:
				a[k] = y[j]
				j += 1
		k += 1
		
	if i < len(x):
			for m in range(i, len(x)):
				a[k] = x[m]
				k += 1
	elif j < len(y):
			for n in range(j, len(y)):
				a[k] = y[n]
				k += 1
	print(a)

mergeSort(cards)
print(cards)