import time, math

primes = [2]
primes_below = {1:[], 2: primes.copy() }

def is_prime(n):
	prime = True
	y = int(math.sqrt(n))
	print(y, primes_below[y])
	for x in primes_below[y]:
		if n%x == 0:
			prime = False
			break
	return prime

def get_primes_below(n):
	for x in range(3, n+1):
		if is_prime(x):
			primes.append(x)
		primes_below[x] = primes.copy()

t1 = time.time()	
get_primes_below(1000)
print(primes)
	
t2 = time.time()

print(t2 - t1)