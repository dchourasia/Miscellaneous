cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
def selectionSort(a):
	loops = 0
	for i in range(len(a)):
		for j in range(i + 1, len(a)):
			loops += 1
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
	print('ran ', loops, ' times for ', len(a), ' size list')
	return a
			

def bubbleSort(a):
		loops = 0
		swapped = True
		c = 0
		while swapped:
			swapped = False
			c += 1
			for n in range(len(a) - c):
				loops += 1
				if a[n] > a[n + 1]:
					swapped = True
					a[n], a[n + 1] = a[n +1], a[n]
		print('ran ', loops, ' times for ', len(a), ' size list')
		return a

		
def recursiveBubbleSort(a, c=0):
			swapped = False
			c += 1
			for n in range(len(a) - c):
				if a[n] > a [n + 1]:
					swapped = True
					a[n], a[n + 1] = a[n +1], a[n]
			if swapped:
				return recursiveBubbleSort(a, c)
			else:
				return a
				

		
#print(selectionSort(cards))
#print(bubbleSort(cards))
print(recursiveBubbleSort(cards))
