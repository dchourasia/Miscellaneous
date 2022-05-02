#1

#print(sum([n for n in range(1, 1000) if n%3 == 0 or n%5 == 0]))

#2
def get_fibonacci():
	x, y = 1, 2
	z = x + y
	limit = 4000000
	#yield x
	yield y
	while z < limit:
		if z%2 == 0:
			yield z
		
		x, y = y, z
		z = x + y
		
#print(sum([n for n in get_fibonacci()]))

#3

def getPrimes(n):
	primes = [2, 3, 5, 7]
	x = 8
	while x <= n:
		#print('starting outer loop')
		isPrime = True
		sqrt = int(x**0.5)
		for y in primes:
			if y > sqrt:
				break
			if x%y == 0:
				isPrime= False
				break
		if isPrime:
			primes.append(x)
		x += 1
	print(primes)
	return primes
				

def findPrimeFactors(n):
	x = 2
	factors = []
	while n > 1:
		if n%x == 0:
			print(x)
			factors.append(x)
			while n%x == 0:
				n = n/x
		x += 1
	print(factors)
	
	
n = 600851475143
#findPrimeFactors(n)

#4
def isPalindrome(n):
	return str(n) == str(n)[::-1]
	
def findLargestPalindrome(n):
	max = int('9'*n)
	span = 100
	palindromes = []
	for m1 in range(max, max - span, -1):
		for m2 in range(max, max - span, -1):
			if isPalindrome(m1*m2):
				palindromes.append(m1*m2)
				
	print(palindromes)
	
def getFactors(n, primes):
	factors = []
	for x in primes:
		if n%x == 0:
			while n%x == 0:
				factors.append(x)
				n /= x
		if n == 1:
			break
	factors = {x: factors.count(x) for x in set(factors)}
	return factors

def mergeMax(d1, d2):
	for p, c in d1.items():
		if p in d2 and c < d2[p]:
			d1[p] = d2[p]
	return d1
				
#findLargestPalindrome(3)

#5
def findMinNumberDivisibleByAll(n):
	primes = getPrimes(n)
	uniqueFactors = {}
	for p in primes:
		uniqueFactors[p] = 0
	print(uniqueFactors)
	for x in range(2, n+1):
		factors = getFactors(x, primes)
		print(factors)
		uniqueFactors = mergeMax(uniqueFactors, factors)
		
	print(uniqueFactors)
	minNum = [x**y for x, y in uniqueFactors.items()]
	import functools
	minNum = functools.reduce(lambda x, y: x*y, minNum)
	print(minNum)
		
		
#findMinNumberDivisibleByAll(20)

#6

def sumSqrDiff(n):
	sumSqr = sum([x**2 for x in range(n+1)])
	sqrSum = sum([x for x in range(n+1)])**2
	
	print(sumSqr - sqrSum)
	
	
#sumSqrDiff(100)

#7
# 10001st prime

def getFirstNprime(n):
	primes = [2, 3, 5, 7, 11]
	x = 12
	while len(primes) < n:
		sq = int(x**0.5)
		isPrime = True
		for p in primes:
			if p <= sq:
				if x%p ==0:
					isPrime = False
					break
			else:
				break
		if isPrime:
			primes.append(x)
		x += 1
	return primes
	
#print(getFirstNprime(10001)[-1])

#8
def getLargestProduct():
		def getSeqProd(x):
			p = 1
			for y in range(13):
				p *= int(n[x + y])
			return p
			
		n = open('num.txt').read().replace('\n', '')
		print(n)
		prods = [getSeqProd(x) for x in range(len(n) - 12)]
		print(max(prods))
		
		
		
		
#getLargestProduct()
	
#9	
# pythogorian triplet
# a2 + b2 = c2
# a +b+c = 1000

def getTriplet():
	def checkTriplet(a, b):
		return a + b + (a**2 + b**2)**0.5 == 1000
		
	triplet = [(a, b) for a in range(250) for b in range(250, 500) if checkTriplet(a,b)] 
	print(triplet)
	a, b = triplet[0]
	print(a*b*(a**2 + b**2)**0.5)
#getTriplet()

#10

def getSumOfPrimesTill(n):
	primes = [2, 3, 5, 7, 11, 13]
	sm = sum(primes)
	next = 14
	while next <= n:
		lim = int(next**0.5)
		isPrime = True
		for p in primes:
			if p > lim:
				break
			if next%p == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(next)
			sm += next
		next += 1
	print(sm)
		
		
#getSumOfPrimesTill(2000000)

def getLargestProductInGrid():
	with open('grid.txt') as grid:
		m = []
		line = grid.readline()
		while line:
			r = [int(n) for n in line.split(' ')]
			m.append(r)
			line = grid.readline()
		
		
	#left right
	mx = -1
	for r in m:
		l = len(r)
		x = max([r[y]*r[y + 1]*r[y + 2]*r[y + 3] for y in range(l - 4)])
		mx = max(x, mx)
	print(mx)
	#up down
	r1 = m[0]
	for c in range(len(r1)):
		x = max([m[r][c]*m[r+1][c]*m[r+2][c]*m[r+3][c]  for r in range(len(m) - 4)])
		mx = max(x, mx)
	print(mx)
	
	#diagonally 0, 0
	rows = len(m)
	cols = len(m[0])
	for r in range(3, len(m)):
		x = max([m[r][c]*m[r-1][c+1]*m[r-2][c+2]*m[r-3][c+3] for c in range(r -2)])
		mx = max(x, mx)
	print(mx)
	#1, 0
	for r in range(3, len(m)):
		x = max([m[r][c]*m[r-1][c-1]*m[r-2][c-2]*m[r-3][c-3] for c in range(cols, cols - r + 2, -1)])
		mx = max(x, mx)
	print(mx)
		
getLargestProductInGrid()
		

			



		

		
	

	
	
	
	
