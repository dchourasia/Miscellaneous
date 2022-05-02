def binarySearch(a, element, s=0, e=None):
	if not e:
		e = len(a) - 1
	if s == e and a[s] == element:
		return e
		
	mid = s + (e - s)//2
	if a[mid] == element:
		return mid
	elif element < a[mid]:
		return binarySearch(a, element, s, mid)
	else:
		return binarySearch(a, element, mid, e)
		
		
def exponentialSearch(a, element):
		exp = 0
		found = False
		while 2**exp < len(a):
			if a[2**exp] > element:
				found = True
				break
			exp += 1
			
		if found:
		   start, end = 2**(exp - 1) if exp > 0 else 0, 2**exp
		   
		else:
		   start,end = 2**exp, len(a) - 1
		   
		#print(start, end)
		return binarySearch(a, element, start,end)
	    
			
		
def interpolationSearch(s, element):
		
		
cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
           
print(exponentialSearch(sorted(cards), '4h'))
