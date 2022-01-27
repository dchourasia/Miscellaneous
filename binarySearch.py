b = [2, 3, 4, 10, 40]
cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As"
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah"
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad"
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]

def binarySearch(a, v, s=0, e=0):
	# assume a is sorted ascending
	e = len(a) - 1 if not e else e
	#if e - s == 1:
		#return s if a[s] == v else e if a[e] == v else -1
	mid = s + int((e - s)/2)
	if a[mid] == v:
		return mid
	elif a[mid] > v:
		return binarySearch(a, v, s=s, e=mid)
	elif a[mid] < v:
		return binarySearch(a, v, s=mid, e=e)
		
cards.sort()
print(cards)
		
x = binarySearch(cards, '5h')
print(x)
x = binarySearch(b, 3)


def jumpSearch(a, v):
	m = jumpBlock = len(a)//2
	# devise a formula for optimal value of jump block to achieve least traversal
	res = -1
	l = len(a)
	m = int(l**0.5)
	print('length , chunk', l, m)
	
	
	
	for i in range(0, l, m):
		#print('i', i)
		e = i + m if i + m < l else l - 1
		if v <= a[e]:
			res = i
			break
		
	if res >= 0:	
		e = res + m if res + m < l else l
		for res in range(res, e):
			if a[res] == v:
				break
					
	return res
	
x = jumpSearch(cards, 'Qh')
print(x)
	
def exponentialSearch(a, v):
	exp = 1
	s = exp
	res = -1
	l = len(a)
	while a[exp] < v:
		s = exp
		exp *= 2
		if exp >= l:
			if v < a[l - 1]:
				exp = l - 1
			break
	if exp < l:
		res = binarySearch(a, v, s, exp)
	return res
	
	
	
print(exponentialSearch(cards, 'Qh'))

		
	