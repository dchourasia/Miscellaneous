#pylint:disable=E0001
cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
arr = [1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17]
           
def printTree(a):
	pass
# child of nth node = 2n + 1, 2n + 2
# parent of the nth node = ceil(n/2) - 1,(n - 1)//2
# level of nth node = 
# leaf nodes : n//2 to n-1
# number of levels : log(n) + 1

def heapify(tree, x, n=-1):
	#heapify done for non-leaf nodes
	# pickup each lowest non-leaf node
	# recurse till root to send max number to top
	left, right, largest, size = 2*x + 1, 2*x + 2, x, len(tree) if n < 0 else n
#	print('size', size)
	if left < size and tree[left] > tree[largest]:
			largest = left
	if right < size and tree[right] > tree[largest]:
			largest = right
	if largest != x:
		#print(x, largest)
		#print('val', tree[x], tree[largest])
		tree[x], tree[largest] = tree[largest], tree[x]
		#this recurses over all the children
		heapify(tree, largest, size)
	


def buildHeap(tree):
	n = len(tree)
	#this loops over all the non-leaf nodes
	for x in range(n//2 - 1, -1, -1):
		heapify(tree, x)
        print(x)
		
def heapsort(tree):
	n = len(tree)
	#heapify once, 
	for x in range(n//2 - 1, -1, -1):
		heapify(tree, x)
	#now max at the top
	for x in range(n - 1, 0, -1):
		#print('heapify', tree)
		# swap first and last, so that max at end
		tree[x], tree[0] = tree[0], tree[x]
	#	print('swap', tree)
		# now heapify the reduced tree root
		heapify(tree, 0, x)
		
def addElementToHeap(heap, x):
	heap.append(x)
	heapify(heap, len(heap) - 1)
#buildHeap(cards)
#print(cards)
buildHeap(arr)
print(arr)
addElementToHeap(arr, 7)
print(arr)
#heapsort(arr)
#print(arr)

