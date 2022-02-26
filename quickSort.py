cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
           
def partition(a, low, high):
	# it should partition on last element as pivot
	# it should rearrange array such that elements less than pivot are before it and greator are after it
	# it should return final index of pivot
	if high - low == 0:
		return
	print('range', low, high)
	print(a)
	
	piv = a[high]
	y = low
	for n in range(low, high):
		if a[n] < piv:
			print('swapping n and y',n, y)
			# move all the smaller elements to beginning of the list so that at the end we know at y index all smaller elements are b3fore and greater elemente are after
			a[n], a[y] = a[y], a[n]
			y += 1
	# now swap yth and pivot so that pivot comes to the balancing point
	
#	if y == low -1:
#			y = low
	a[high], a[y] = a[y], a[high]
			
			
	print(a)
	print('p', y)
	return y
	
def quickSort(a, low, high):
	if low < high:
		p = partition(a, low, high)
		#print('p', p, low, high)
		if p is not None and p > low:
			#print(low, p - 1)
			quickSort(a, low, p - 1)
		if p is not None and p < high:
			#print(p + 1, high)
			quickSort(a, p + 1, high)
		

quickSort(cards, 0, len(cards) - 1)
#print(cards, len(cards))
	