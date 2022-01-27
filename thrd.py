def worker(l):
	l.extend([1, 2])
	
	
from threading import Thread

l =[]
a = Thread(target=worker, args=(l, ))
b = Thread(target=worker, args=(l, ))

a.start()
b.start()
a.join()
b.join()

print(l)

