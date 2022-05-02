# complete tree
# children 2n + 1, 2n + 2
# parent (n - 1)//2
# leaf nodes n//2

def inOrder(cards, idx=0):
	if 2*idx + 1 < len(cards):
		inOrder(cards, 2*idx + 1)

	print(cards[idx])
	
	if 2*idx + 2 < len(cards):
		inOrder(2*idx + 2)
	

	










cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]