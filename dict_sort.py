d = {1:2, 4:3, 3:3, 6:4, 8:2}

k = sorted(d, key=lambda x: str(d[x]) + str(x))
print(k)

d = {x:d[x] for x in k}
print(d)


