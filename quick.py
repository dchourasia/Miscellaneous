def quickSort(a, s=0, e=None):
	if s == e:
		return 
	
	if not e:
		e = len(a) - 1
	#partition
	# recursion
	p = partition(a, s, e)
	
	if p + 1 < e:
		quickSort(a, p + 1, e)
	if p - 1 > s:
		quickSort(a, s, p - 1)
	
	
def partition(a, s, e):
	if e - s <= 0:
		return 
	p = e
	print('before', cards)
	print(s, e)
	for i in range(e - 1, s - 1, - 1):
		if a[i] > a[p]:
			print(a[i], a[p])
			a[p - 1], a[i] = a[i], a[p - 1]
			a[p], a[p - 1] = a[p - 1], a[p]
			#print('mid', a)
			
			p -= 1
			print(a)
	print(p)
	print('after', cards)
	return p
	
	
cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
quickSort(cards)
#print(cards)
#partition(cards, 0, len(cards) - 1)
			
			
	