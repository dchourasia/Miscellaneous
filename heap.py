cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
 # children 2n + 1,2n + 2
 # parent (n - 1)//2
 # levels = log(n) + 1
 
def heapify(a, m, e=None):
 	largest = m
 	e = len(a) if not e else e
 	left, right = 2*m + 1, 2*m + 2
 	if left < e and a[left] > a[largest]:
 		largest = left
 	if right < e and a[right] > a[largest]:
 		largest = right
 		
 	a[largest], a[m] = a[m], a[largest]
 	
 	if largest != m:
 		heapify(a, largest, e)
 	
def heapSort(a):
 	n = len(a)
 	for x in range(n//2 -1, -1, -1):
 		heapify(a, x, n)
 	
 	for e in range(n - 1, 0, -1):
 		a[e], a[0] = a[0], a[e]
 		heapify(a, 0, e)
 	
 	
heapSort(cards)
print(cards)