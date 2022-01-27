s=5
e=25000

lst=[1,2]

def getPrimes(n):
	for i in range(3,n):
		res=True
		for j in lst[1:]:
			if i%j == 0:
				res=False
				break
		if res:
			lst.append(i)
			
def getPrimesInRange(s, e):
	getPrimes(s)
	prm= []
	for i in range(s,e+1):
		res=True
		for j in lst[1:]+prm:
			if i%j == 0:
				res=False
				break
		if res:
			prm.append(i)
		
	return prm
	
			
def isprime(n):
	res=True
	for i in range(2,n):
		if n%i == 0:
			res=False
			break
	return res
	
	
#primes= [n for n in range(s,e) if isprime(n)]

primes=getPrimesInRange(s,e)
print(primes)

#getPrimes(7)
#print(lst)
	
	
	