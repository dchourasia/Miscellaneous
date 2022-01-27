inp = '23, 45, 34, 76, 98'

lst = [x.strip() for x in inp.split(',')]
tup = tuple(lst)

print(lst)
print(tup)