#factorial

from functools import reduce
n=8
fact=reduce((lambda x, y: x*y), [x for x in range(1, n+1)])

print(fact)