cards = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc"
           ]
           
sub = ["10h","Jh","Qh","Kh","Ah"]

cards.sort()
sub.sort()

print(cards)
print(sub)

def subListSearch(parent, child):
	res = True
	for e in parent:
		if e == child[0]:
			child.pop(0)
		if len(child) == 0:
			break
		#print(e, child[0])
		if e > child[0]:
			res = False
			break

	return res
	
print(subListSearch(cards, sub))
'''
curr = 0
started = 0
res = False
for c in cards:
	print(c, curr)
	if started:
		if c == sub[curr]:
			curr += 1
		else:
			curr == 0
			started = 0
		if curr == len(sub) - 1:
			res = True
			break
	if not started and c == sub[0]:
		started = 1
		curr += 1
		
		
print(res)
'''
	
	
